import io
import json
import oci

def handle(ctx, data: io.BytesIO=None):
    # Check if there is data in the input
    if data is None:
        return json.dumps({"message": "No data received"})

    # Read the binary data
    try:
        binary_data = data.read()
        size = len(binary_data)
        
        # Authenticate with OCI services using Resource Principal
        signer = oci.auth.signers.get_resource_principals_signer()
        # Here you can use the signer to authenticate calls to other OCI services
        
        # Example: Call to Document Understanding API (replace with actual call)
        # client = oci.ai_vision.AIServiceVisionClient(config={}, signer=signer)
        # response = client.your_api_call_method()

        # For this example, we are just returning the size of the data received.
        return json.dumps({"message": "Received binary data", "size": size})
    except Exception as e:
        return json.dumps({"error": str(e)})
