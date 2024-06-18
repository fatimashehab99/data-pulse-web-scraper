import json


# this function is used to get post title and post tags
def getPostTitle(soup):
    post_tags = []
    post_title = ""
    div_titles = soup.find_all("meta", property="og:title")  # get div titles

    if div_titles:
        post_title = div_titles[0].get('content')  # get post title
        # Loop through the rest and print their content to get the post tags
        for div_title in div_titles[1:]:
            content = div_title.get("content")
            if '|' in content:
                tags = content.split('|')[1:]  # Extract the part after the last '|'
                # Strip any leading/trailing whitespace from categories and add to post_categories
                post_tags.extend([tag.strip() for tag in tags])
    return {"post_title": post_title, "post_tags": post_tags}


# this function is used to get the post type
def getPostType(soup):
    return (soup.find("meta", property="og:type")).get("content")


# this function is used to get the domain
def getDomain(soup):
    return (soup.find("meta", property="og:site_name")).get("content")


# this function is used to get the post description
def getPostDescription(soup):
    return (soup.find("meta", property="og:description")).get("content")


# this function is used to get the post image
def getPostImage(soup):
    return (soup.find("meta", property="og:image")).get("content")


# this function is used to get the  post currency
def getPostCurrency(soup):
    return (soup.find("meta", property="og:price:currency")).get("content")


# this function is used to get the post price and discount price
def getPostPrice(soup):
    post_discount_price = "$0 USD"
    div_price = soup.find("div", class_="t4s-product-price")
    del_tag = div_price.find("del")  # Find the <del> tag within this div and extract the price
    if del_tag:
        post_base_price = del_tag.text
        ins_tag = div_price.find("ins")  # Find the <ins> tag within this div and extract the discount price
        if ins_tag:
            post_discount_price = ins_tag.text
    else:
        post_base_price = div_price.text
    return {"post_base_price": post_base_price, "post_discount_price": post_discount_price}


# this function is used to get the post vendor
def getPostVendor(soup):
    vendor_name_div = soup.find("div", class_="t4s-vendor-wrapper")
    return vendor_name_div.find("span").find("a").text


# this function is used to get the post id
def getPostId(soup):
    product_id_div = soup.find("div", class_="t4s-col-item t4s-col-12 t4s-main-area")
    product_data = product_id_div.find("div").get("data-product-featured")  # get the product data array
    product_data_json = json.loads(product_data)  # Parse JSON string to dictionary
    return product_data_json["id"]  # Extract the id


# this function is used to get the post items
def getPostItems(soup):
    items_dev = soup.find("div", class_="t4s-swatch__list")  # Get the items div
    items = []
    if items_dev:
        # Loop over each swatch item within the items div
        for item in items_dev.find_all("div", class_="t4s-swatch__item"):
            data_value = item.get("data-value")  # Extract the data-value attribute
            # Add the data-value to the list if it exists
            if data_value:
                items.append(data_value)
    return items
