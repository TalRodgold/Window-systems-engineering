import enum

RECEIPES_API = "https://edamam-recipe-search.p.rapidapi.com/api/recipes/v2"
RECEIPES_QUERYSTRING = {"type":"public","co2EmissionsClass":"A+","field[0]":"uri","q":"","beta":"true","random":"true"}
RECEIPES_HEADERS = {
	"Accept-Language": "en",
	"X-RapidAPI-Key": "e4cb194fedmsh8f5e57ba5fc557cp16248ajsn0d64d197f11a",
	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
}