import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Load your model (adjust path as needed)
model_path = r'C:\Users\piranavan\Desktop\FDM HR\pickle2.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@api_view(['POST'])
def predict(request):
    try:
        # Extract data from the request
        data = request.data
        input_data = [
            data['city_development_index'],
            data['relevant_experience'],  # Corrected spelling
            data['education_level'],
            data['experience'],
            data['last_new_job']
        ]

        # Predict using the model
        prediction = model.predict([input_data])

        # Return the prediction result
        return Response({'prediction': prediction[0]}, status=status.HTTP_200_OK)

    except KeyError as e:
        return Response({'error': f'Missing key: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
