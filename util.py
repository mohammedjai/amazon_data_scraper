def product_name_price(soupe):
    name = soupe.find('span',{'id':'productTitle'}).text
    price_class = soupe.find('span',{'class':'a-price a-text-normal aok-align-center reinventPriceAccordionT2'})
    price = price_class.find('span',{'class':'a-offscreen'}).text
    print('n/a')
    data = {
        'Name':name,
        'Price':price,
    }
    return data
def product_details(soupe):
    details_class = soupe.find('div',{'class':'a-section a-spacing-small a-spacing-top-small'})
    details_line = details_class.find_all('tr')
    for info in details_line:
        detail = (info.text)
        data = {
            'Details':detail
        }
        return data
def product_info(soupe):
    item_details = soupe.find('table',{'id':'productDetails_detailBullets_sections1'})
    if item_details:
        all_trs = item_details.find_all('tr')
        for tr in all_trs:
            product_info = (tr.text)
            list = product_info
            data = {
                'Info':list
            }
        return data
    else:
        print('Info : Not Available')

def product_rating(soupe):
    rating = soupe.find('span',{'class':'a-icon-alt'}).text
    global_rating = soupe.find('span',{'id':'acrCustomerReviewText'}).text
    percent_rating = soupe.find_all('td',{'class':'a-text-right a-nowrap a-nowrap'})
    stars_5 = percent_rating[0].text
    stars_4 = percent_rating[1].text
    stars_3 = percent_rating[2].text
    stars_2 = percent_rating[3].text
    stars_1 = percent_rating[4].text
    data = {
        'Rating':rating,
        'Rating count':global_rating,
        '5 Stars':stars_5,
        '4 Stars':stars_4,
        '3 Stars':stars_3,
        '2 Stars':stars_2,
        '1 Stars':stars_1
    }
    return data
def product_images(soupe):
    image = soupe.find('div',{'id':'imageBlock'})
    pic = image.find_all('span',{'class':'a-button-text'})
    for img in pic:
        try:
            images = img.find('img')
            images_url = images.get('src')
            data = {
                'Picturs':images_url
            }
            return data
        except Exception:
            print('Product Image : Not Availabel')
def product_id(soupe):
    id_element = soupe.find('ul',{'class':'a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal dimension-values-list'})
    if id_element:
        product_id = id_element.find_all('li',{'data-asin':True})
        for id in product_id:
            ids = id.get('data-asin')
            data = {
                'Product ID':ids
            }
            return data
    else:
        print('Product ID : Not Availabel')
        

