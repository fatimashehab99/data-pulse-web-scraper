# this function is used to get post title and post tags
def getPostTitle(soup):
    post_tags = []
    post_title = ""
    # get div titles
    div_titles = soup.find_all("meta", property="og:title")
    if div_titles:
        # get post title
        post_title = div_titles[0].get('content')

        # Loop through the rest and print their content to get the post tags
        for div_title in div_titles[1:]:
            content = div_title.get("content")
            if '|' in content:
                # Extract the part after the last '|'
                tags = content.split('|')[1:]
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
    return soup.find("div", class_="t4s-product-price").text


# this function is used to get the post vendor
def getPostVendor(soup):
    vendor_name_div = soup.find("div", class_="t4s-vendor-wrapper")
    return vendor_name_div.find("span").find("a").text
