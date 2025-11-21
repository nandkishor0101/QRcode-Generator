import qrcode

#taking UPI Id as a input

upi_id = input("ENter Your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#pa = whom you want to pay  #pn = reciepent name # am = amount #cu = currency #tn = payment message

#Defining the payment url based on UPI ID and the payment app
#YOU can modify these urls based on payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create qrcode for each payment pp

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#SAve the QR code to image file(optional)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the qr codes(you may need to instal PIL/Pillow library)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()