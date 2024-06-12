

from typing import Optional, Sequence, Union

from starlette.requests import Request
from starlette.responses import (
    FileResponse,
    JSONResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
)



def _serve_file(request: Request) -> Response:
    from libcloud.storage.types import ObjectDoesNotExistError
    from sqlalchemy_file.storage import StorageManager

    try:
        storage = request.path_params.get("storage")
        file_id = request.path_params.get("file_id")
        file = StorageManager.get_file(f"{storage}/{file_id}")
        if file.object.driver.name == "Local Storage":
            """If file is stored in local storage, just return a
            FileResponse with the fill full path."""
            return FileResponse(
                file.get_cdn_url(), media_type=file.content_type, filename=file.filename  # type: ignore
            )
        if file.get_cdn_url() is not None:  # pragma: no cover
            """If file has public url, redirect to this url"""
            return RedirectResponse(file.get_cdn_url())  # type: ignore
        """Otherwise, return a streaming response"""
        return StreamingResponse(
            file.object.as_stream(),
            media_type=file.content_type,
            headers={"Content-Disposition": f"attachment;filename={file.filename}"},
        )
    except ObjectDoesNotExistError:
        return JSONResponse({"detail": "Not found"}, status_code=404)

