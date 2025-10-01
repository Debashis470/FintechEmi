from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EMI(APIView):
    def post(self, request):
        # Get data from request
        loan_amount = request.data.get("loan_amount")
        interest_rate = request.data.get("interest_rate")  # annual %
        tenure_years = request.data.get("tenure_years")  # in years

        # Validate required fields
        if loan_amount is None or interest_rate is None or tenure_years is None:
            return Response({"error": "loan_amount, interest_rate, and tenure_years are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            P = float(loan_amount)
            R = float(interest_rate) / 12 / 100  # monthly interest rate
            N = int(tenure_years) * 12  # total months

            # EMI calculation formula
            emi = P * R * (1 + R) ** N / ((1 + R) ** N - 1)
            emi = round(emi, 2)
        except (ValueError, ZeroDivisionError):
            return Response({"error": "Invalid input values"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "loan_amount": P,
            "interest_rate": interest_rate,
            "tenure_years": tenure_years,
            "emi": emi
        })
