"""
Test cases for Falcon Web Framework simulating http request from client.

"""
import falcon
from falcon import testing
import pytest
from webscraper.app import app

@pytest.fixture
def client():
    return testing.TestClient(app)

def test_get_valid_app(client):
    # Expected app
    app =  {
    "name": " Livetopia: Party!",
    "version": " 1.3.335",
    "downloads": " 1",
    "release_date": " 2024-02-06 14:30:13",
    "description": "Livetopia: Party! is an open world mmo party game that's full of exciting surprises! It's a modern city by the sea, and you'll get to meet friends from all around the world. You can be whoever you want and do whatever you like. \nInvite your friends to have party and explore more in this open world!\n\n☆Explore!\nPlay a role as a doctor, firefighter, or builder. You can also become a rockstar and play your guitar on stage, drive a go-kart around the city, or even pretend to be a scary zombie and give your friends a shock. \n\n☆Create!\nCreate your own wonderful map in the workshop and wait for others to visit. You'll have opportunities to get multiple rewards and glories.\n\n☆Make Friends!\nDiscover new friends, chat and hang out with them in real time! Build-in mini-games allow you to show off your amazing talents to your friends and to the world!\n\n☆Play Dress-Up and Home Design!\nLivetopia: Party! offers over 100 costumes and accessories for you to create your very own style! You can also decorate and build your perfect house with any furniture you like. \n\n☆Adopt Pets!\nAdopt adorable pets and become their best friend! Play games with them and go on exciting adventures together, train your pets to become powerful fighters, or simply enjoy cuddling with them. And guess what? You can even transform into your pets and explore the world from their points of view!\n\nTo learn more about Livetopia: Party!, please visit:\nInstagram: https://www.instagram.com/livetopiaparty_official\nFacebook: https://www.facebook.com/LivetopiapartyTheGame\nTiktok: https://www.tiktok.com/@livetopiaparty_official\nYoutube: https://www.youtube.com/@Livetopiaparty_Mobile\nDiscord: https://discord.gg/livetopiaparty"
        }
    params = {}
    params["url"] = "https://livetopia-party.en.aptoide.com/app"
    result = client.simulate_get('/aptoideapp/', params=params)
    assert result.json == app

def test_get_invalid_url_format(client):
    # Expected error message
    error =  {"error": "Invalid url format input"}
    params = {}
    params["url"] = "x"
    result = client.simulate_get('/aptoideapp/', params=params)
    assert result.json == error

def test_get_invalid_url(client):
    # Expected error message
    error =  {"error": "Error getting html: Not Found"}
    params = {}
    params["url"] = "https://livetopia-party.en.aptoide.com/appXX"
    result = client.simulate_get('/aptoideapp/', params=params)
    assert result.json == error

def test_get_valid_url_format_invalid_aptoide_url(client):
    # Expected error message
    error =  {"error": "Error scraping html. No match found for attribute: name"}
    params = {}
    params["url"] = "https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en_CA&gl=US"
    result = client.simulate_get('/aptoideapp/', params=params)
    assert result.json == error