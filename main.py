import requests
import img2pdf
import os

def get_data():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.754 (beta) Yowser/2.5 Safari/537.36",
         "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
    }
    img_list = []
    for i in range (1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response =req.content

        
        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Dowloaded{i} of 48")
    
    print("#"*20)
    print(img_list)


    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
    
    print("PDF file created")

def write_to_pdf():
    # print(os.listdir("media"))
    img_list =[f"media/{i}.jpg" for i in range(1,49)]

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
    
    print("PDF file created")


    

    
    

def main():
    get_data()   

if __name__ =="__main__":
    main()








    
