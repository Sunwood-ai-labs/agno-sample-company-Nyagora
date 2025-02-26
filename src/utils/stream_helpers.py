def update_streaming_response(response_placeholder, full_response_text):
    response_placeholder.markdown(full_response_text)

def stream_response(response_generator):
    full_response_text = ""
    for chunk in response_generator:
        if chunk.content is not None:
            full_response_text += chunk.content
            yield full_response_text  # Yield the updated response text for streaming
            update_streaming_response(response_placeholder, full_response_text)  # Update the placeholder
    return full_response_text  # Return the complete response at the end