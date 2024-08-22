## dork.py is the script
## search_reusults.json are the results of running this method on ~100 products
## urls.py are the URLs I used to run the test

### This script calls the google search console API in the same way that a google dork query works. It then scrapes the meta data for the URL that gets returned. 

#### Lets say you're looking for the product "Rehna Long Sleeve Top White" on Princess Pollys website. You can narrow down your google search results and get an more accurate match by searching for: 

#### site:princesspolly.* Rehna Long Sleeve Top White

#### You would get back this URL: https://us.princesspolly.com/products/rehna-long-sleevetop-white?srsltid=AfmBOorWBj4vXETbtj147gse2bSTQqJbZwVCBgsVbmr2FEO3jHfHSy-1

#### When running this script, you get this: 

},
    "site:princesspolly.* Rehna Long Sleeve Top White": {
        "kind": "customsearch#result",
        "title": "Rehna Long Sleeve Top White",
        "htmlTitle": "<b>Rehna Long Sleeve Top White</b>",
        "link": "https://us.princesspolly.com/products/rehna-long-sleevetop-white",
        "displayLink": "us.princesspolly.com",
        "snippet": "Description ... Made with a reclaimed nylon blend, this 'fit was created with fabrics recovered from the manufacturing process. Read more about our Lower Impact\u00a0...",
        "htmlSnippet": "Description ... Made with a reclaimed nylon blend, this &#39;fit was created with fabrics recovered from the manufacturing process. Read more about our Lower Impact&nbsp;...",
        "formattedUrl": "https://us.princesspolly.com/products/rehna-long-sleevetop-white",
        "htmlFormattedUrl": "https://us.princesspolly.com/products/<b>rehna</b>-<b>long</b>-<b>sleevetop</b>-<b>white</b>",
        "pagemap": {
            "offer": [
                {
                    "pricecurrency": "USD",
                    "price": "50.0",
                    "availability": "http://schema.org/InStock"
                }
            ],
            "cse_thumbnail": [
                {
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKssj2tnakmK4A7vufYXuFdmfb-Zvye58mBEpaQefez2UyFkUymMHkcMLM&s",
                    "width": "193",
                    "height": "261"
                }
            ],
            "product": [
                {
                    "image": "//us.princesspolly.com/cdn/shop/files/0-modelinfo-olivia-us2_7eda532a-6c56-4854-ba81-4fa30ff30f3e.jpg?crop=center&height=81&v=1701227575&width=600",
                    "name": "Rehna Long Sleeve Top White",
                    "description": "Long sleeve top V neckline, pinched detail at bust, split hem Good stretch, fully lined, sheer Princess Polly Lower Impact 86% reclaimed nylon 14% elastane Cold gentle machine wash",
                    "sku": "131969-1231713",
                    "brand": "Princess Polly Lower Impact",
                    "url": "https://us.princesspolly.com/products/rehna-long-sleevetop-white"
                }
            ],
            "review": [
                {
                    "ratingstars": "5.0",
                    "reviewdate": "2024-06-26T03:34:30.000Z",
                    "reviewer": "Madeline P."
                },
                {
                    "name": "Gorgeous top! Have received so",
                    "reviewbody": "Gorgeous top! Have received so many compliments wearing it!\ud83e\udef6 highly recommend",
                    "datepublished": "2024-06-26T03:34:30.000Z"
                },
                {
                    "name": "a little loose in the",
                    "reviewbody": "a little loose in the shoulders. good quality, thick material. had to wear a strapless bra because shoulders would not cover straps at all",
                    "datepublished": "2024-04-06T15:31:04.000Z"
                },
                {
                    "name": "great quality. It fits well",
                    "reviewbody": "great quality. It fits well but tight on arms",
                    "datepublished": "2024-03-25T19:37:44.000Z"
                },
                {
                    "name": "Fit perfectly!! Love the top",
                    "reviewbody": "Fit perfectly!! Love the top",
                    "datepublished": "2024-03-06T14:32:06.000Z"
                },
                {
                    "name": "Material is so great it",
                    "reviewbody": "Material is so great it reminds me of skims. Super thick material and not see through!",
                    "datepublished": "2024-02-18T18:11:36.000Z"
                },
                {
                    "name": "I love this top! The",
                    "reviewbody": "I love this top! The quality is thick so i didjt need a bra, and it wasnt see through. So cute snd good material",
                    "datepublished": "2024-02-13T14:58:17.000Z"
                },
                {
                    "name": "easy going out top. automatically",
                    "reviewbody": "easy going out top. automatically elevates a plain, boring outfit.",
                    "datepublished": "2024-02-11T14:53:06.000Z"
                },
                {
                    "name": "Beautiful, high quality shirt.",
                    "reviewbody": "Beautiful, high quality shirt.",
                    "datepublished": "2023-12-17T17:57:59.000Z"
                }
            ],
            "person": [
                {
                    "name": "Madeline P."
                },
                {
                    "name": "Aly M."
                },
                {
                    "name": "Jessica L."
                },
                {
                    "name": "Reesha G."
                },
                {
                    "name": "Brooklyn F."
                },
                {
                    "name": "Audrey H."
                },
                {
                    "name": "MARAH J."
                },
                {
                    "name": "Abigail T."
                }
            ],
            "aggregaterating": [
                {
                    "ratingvalue": "4.7",
                    "itemreviewed": "Rehna Long Sleeve Top White",
                    "ratingcount": "10"
                }
            ],
            "organization": [
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                },
                {
                    "name": "Princess Polly"
                }
            ],
            "rating": [
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "4"
                },
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "5"
                },
                {
                    "ratingvalue": "5"
                }
            ],
            "metatags": [
                {
                    "og:image": "http://us.princesspolly.com/cdn/shop/files/0-modelinfo-olivia-us2_7eda532a-6c56-4854-ba81-4fa30ff30f3e_1024x1024.jpg?v=1701227575",
                    "theme-color": "#000000",
                    "og:type": "product",
                    "twitter:card": "summary_large_image",
                    "twitter:title": "Rehna Long Sleeve Top White",
                    "og:site_name": "Princess Polly USA",
                    "og:price:amount": "50.00",
                    "og:title": "Rehna Long Sleeve Top White",
                    "og:price:currency": "USD",
                    "shopify-checkout-api-token": "efe3d0c047d3938f4cf11178bb292a5b",
                    "og:description": "Shop Rehna Long Sleeve Top White at Princess Polly. Buy now, pay later with Afterpay. Enjoy free shipping & returns. T&C's apply.",
                    "og:image:secure_url": "https://us.princesspolly.com/cdn/shop/files/0-modelinfo-olivia-us2_7eda532a-6c56-4854-ba81-4fa30ff30f3e_1024x1024.jpg?v=1701227575",
                    "facebook-domain-verification": "8vnaz3jjg8hljhpve6lawisjfdzshv",
                    "trustpilot-one-time-domain-verification-id": "251c1143-85ab-4343-acd6-d1530d51f34f",
                    "twitter:site": "@",
                    "viewport": "width=device-width,initial-scale=1",
                    "shopify-digital-wallet": "/6186270804/digital_wallets/dialog",
                    "twitter:description": "Shop Rehna Long Sleeve Top White at Princess Polly. Buy now, pay later with Afterpay. Enjoy free shipping & returns. T&C's apply.",
                    "og:url": "https://us.princesspolly.com/products/rehna-long-sleevetop-white",
                    "tapcart-banner:appicon": "https://storage.googleapis.com/tapcart-150607.appspot.com/17d4d6b6b521f29f7837690f4736e088_AppIconpng.png"
                }
            ],
            "cse_image": [
                {
                    "src": "http://us.princesspolly.com/cdn/shop/files/0-modelinfo-olivia-us2_7eda532a-6c56-4854-ba81-4fa30ff30f3e_1024x1024.jpg?v=1701227575"
                }
            ],
            "hproduct": [
                {
                    "fn": "Rehna Long Sleeve Top White",
                    "description": "Long sleeve top V neckline, pinched detail at bust, split hem Good stretch, fully lined, sheer Princess Polly Lower Impact 86% reclaimed nylon 14% elastane Cold gentle machine wash",
                    "photo": "//us.princesspolly.com/cdn/shop/files/0-modelinfo-olivia-us2_7eda532a-6c56-4854-ba81-4fa30ff30f3e.jpg?crop=center&height=81&v=1701227575&width=600",
                    "currency": "AUD",
                    "currency_iso4217": "36",
                    "url": "https://us.princesspolly.com/products/rehna-long-sleevetop-white"
                }
            ],
            "listitem": [
                {
                    "item": "Tops",
                    "name": "Tops",
                    "position": "1"
                },
                {
                    "item": "Crop Tops",
                    "name": "Crop Tops",
                    "position": "2"
                },
                {
                    "item": "https://us.princesspolly.com/products/rehna-long-sleevetop-white",
                    "name": "Rehna Long Sleeve Top White",
                    "position": "3"
                }
            ]
        }
    },

