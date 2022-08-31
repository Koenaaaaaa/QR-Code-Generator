#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install all the libraries needed
# Create a function that collects a text and converts it to a QR code
# Save the QR code as an image
# Run


# In[7]:


import qrcode


# In[8]:


def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")
    


# In[9]:


generate_qrcode("kntsoftwares.co.za")


# In[ ]:




