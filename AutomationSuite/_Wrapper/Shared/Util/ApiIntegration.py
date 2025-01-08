import requests


def upload_file_with_form_data(file_path, token):
    """
    Upload an Excel file using a POST API with form-data and Bearer Token.

    Args:
        file_path (str): Path to the Excel file to upload.
        token (str): Bearer Token for authorization.

    Returns:
        dict: Response data or error details.
    """
    url = "https://chorusdev.cogninelabs.com/api/dfttcr/excelfileimport"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Open the file in binary mode and attach it as form-data
    with open(file_path, "rb") as file:
        files = {
            "file": file,  # The key here is the form-data key expected by the API
        }
        try:
            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 200:
                return response.json()  # Return JSON response
            else:
                return {"error": response.text}  # Return error details
        except requests.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}


# Example Usage
file_path = "C:/Users/Anupama Saranu/Desktop/Sample Defect Sheet.xlsx"
bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyIsImtpZCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyJ9.eyJhdWQiOiJhcGk6Ly9iZWZlOGI4Zi05NTZhLTQ3ZjMtYmE1NS03YzYxZTM2ZTkzZWIiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zMDMzNjQyZC02YWRmLTRhYzYtYmJjNS01MTFiNDJiYzVmMDAvIiwiaWF0IjoxNzM2MzE2MjkyLCJuYmYiOjE3MzYzMTYyOTIsImV4cCI6MTczNjMyMTY4NSwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhZQUFBQVUrVDBOYVJPYmRJcURsM0c4VTRJNHRsTTlSbStBVVVRc21jenZqY3RlRkVpUTNEM1BWNE5FbTJWUUJ4YXYyb2EiLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiYmVmZThiOGYtOTU2YS00N2YzLWJhNTUtN2M2MWUzNmU5M2ViIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJTYXJhbnUiLCJnaXZlbl9uYW1lIjoiQW51cGFtYSIsImlwYWRkciI6IjE4Mi43Mi4xNzUuMTQiLCJuYW1lIjoiQW51cGFtYSBTYXJhbnUiLCJvaWQiOiI0ZGI0MzQ1Ni1iYzJmLTQyZmItYmI0ZS00ZDM4NDM4MTI5YmMiLCJyaCI6IjEuQVZZQUxXUXpNTjlxeGtxN3hWRWJRcnhmQUktTF9yNXFsZk5IdWxWOFllTnVrLXVmQU50V0FBLiIsInNjcCI6ImFwcCIsInN1YiI6IkMyVGFWNGJVaDQwR0xqSkhHcld3d0NyYXFmRmFWdENKTFdIY0tiU2tsV3MiLCJ0aWQiOiIzMDMzNjQyZC02YWRmLTRhYzYtYmJjNS01MTFiNDJiYzVmMDAiLCJ1bmlxdWVfbmFtZSI6ImFudXBhbWEuc2FyYW51QGNvZ25pbmUuY29tIiwidXBuIjoiYW51cGFtYS5zYXJhbnVAY29nbmluZS5jb20iLCJ1dGkiOiJwSFRGdU15N3IwdWRDRzVrN0lKSUFBIiwidmVyIjoiMS4wIn0.nJnATARSd_95sQCAzvX_o18QERC9tekH_9BXh3Dzrdvsy35Wke9emy6jtz8qSEvX5BMjiTXz1XlAuxOUyRLvekNCVunEvqZqqETnoQKUZsHpZT5s-d3MdtNe2T7WJzmfuQ4g_p4hKYi7nHQTzbC6QCwpTT3MYRJOJWgRJBaJp8co23BpmC4WzLXyqjJaMnwSjG2KHh_7cTSbt8k2qsPGetHIniFGqUEu21mjkn6yPR96USgMPRONfsSdGft4nMwjj4FXOUWAQsVlqzrr5WnDQ_R6h4O5N8zXR1ct6sF7u3VOS6-ZQ-qdAxw4PSQVWDIQXdXJ-bMf08srdVAocXxNUw"

result = upload_file_with_form_data(file_path, bearer_token)
print(result)
