import io
import oci
from fdk import response

def handler(ctx, data: io.BytesIO=None):
    try:
        # Initialize the AI Vision Service client with Resource Principal Signer
        signer = oci.auth.signers.get_resource_principals_signer()
        ai_vision_client = oci.ai_vision.AIVisionClient(config={}, signer=signer)

        # Example: Call a method from the AI Vision service (adjust as needed)
        # For instance, analyze an image, get a model, etc.
        # response_data = ai_vision_client.some_ai_vision_method()
        response_data = "{\"message\":\"Good morning Christian!\"}"

        return response.Response(
            ctx, response_data=response_data,
            headers={"Content-Type": "application/json"}
        )

    except Exception as e:
        return response.Response(
            ctx, response_data={"error": str(e)},
            headers={"Content-Type": "application/json"}
        )
