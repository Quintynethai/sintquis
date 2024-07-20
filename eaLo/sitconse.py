   try:
       articles_data = response.json()
   except JSONDecodeError as e:
       print(f"Error decoding JSON: {e}")
   except Exception as e:
       print(f"Error fetching response: {e}")
   