from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from backend.utils.audio_utils import (
    extract_audio_from_video,
    transcribe_audio,
    generate_voice_response
)
import uuid
import os
import shutil

router = APIRouter(prefix="/assistant", tags=["Voice Assistant"])


@router.post("/voice", summary="🎙️ Ask via voice or video, get spoken response")
async def voice_shopping_assistant(file: UploadFile = File(...)):
    """
    Accepts voice or video file, converts it to text,
    answers the query using SmartBiz, and returns audio response.
    """

    temp_dir = "temp_audio"
    os.makedirs(temp_dir, exist_ok=True)

    file_id = str(uuid.uuid4())
    input_path = os.path.join(temp_dir, f"{file_id}_{file.filename}")
    output_path = os.path.join(temp_dir, f"{file_id}.wav")

    # Save input file
    try:
        with open(input_path, "wb") as f:
            f.write(await file.read())
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to upload file")

    try:
        # 1. Extract audio (if needed)
        await extract_audio_from_video(input_path, output_path)

        # 2. Transcribe to text
        transcript = await transcribe_audio(output_path)

        # 3. Generate voice reply text
        response_text = f"Umeuliza kuhusu: {transcript}. Hii bidhaa inapatikana kwenye stock yetu."

        # 4. Convert response to voice
        voice_path = await generate_voice_response(response_text, file_id)

        return {
            "message": response_text,
            "transcript": transcript,
            "voice_reply_url": f"/static/responses/{file_id}.mp3"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Voice Assistant Error: {str(e)}")

    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
