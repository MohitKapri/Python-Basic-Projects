import qrcode

#Taking upi_id as a input from the user

upi_id = input("Enter your UPI ID =")

##upi://pay?pa=UPI_ID&pn=NAME&am=amount&cu=CURRENCY&tn=MESSAGE
phonepe_url =f'upi://pay?pa={upi_id}&pn=recipient%20&NAME'
paytm_url =f'upi://pay?pa={upi_id}&pn=recipient%20&NAME'
google_pay_url =f'upi://pay?pa={upi_id}&pn=recipient%20&NAME'

#create qr code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Display the qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

