import requests as re 
import streamlit as st
from PIL import Image
from io import BytesIO
# url='https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=live_CDDPwz8R2fd5uzChj7Ns9npUQcpZuPPzScXp0Y9NWysKOEbG410IX7tooOMhxfUV'

def get_pic():
    
    url='https://api.thecatapi.com/v1/images/search'
    response=re.get(url)
    
    if response.status_code == 200:
        print('success:',response.json())
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        
    data=response.json()
    # print(data)
    
    url_data=data[0]['url']
    # for i in url_data:
    #     print(i)
    return url_data
    
def fetch_img(url_data):
    img_d=re.get(url_data).content
    img=Image.open(BytesIO(img_d))
    
    return img    

# def image():
#     img_url = get_pic()
#     img=fetch_img(img_url)
#     st.image(img, caption='Cat Image', use_column_width=True)
#     st.write("Button clicked!")

st.title("Wlcome to cat heaven")

# image()    

# if st.button('Get a new cat!!'):
#    image()

# while True:
#     image_url = get_pic()  # Get the first cat image URL
#     img = fetch_img(image_url)  # Fetch and open the image
#     st.image(img, width=700)
#     break
#     print("lOOP DONE")    
                
st.markdown("<br><br><br>", unsafe_allow_html=True)  

# Button to fetch a new cat image at the bottom
if st.button('Get a new cat!', use_container_width=True):
    image_url = get_pic()  
    img = fetch_img(image_url)  
    st.image(img, width=700)
    # st.write("Button clicked!")








                            