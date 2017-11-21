PARAMETRES OBLIGATOIRES: 
	part :	Précise si c'est une liste séparé en un ou plusieurs propriétes 
		- "snippet" (PAR DEFAULT)

FILTRES:
	forContentOwner : Booléen qui filtre les vidéos qui appartiennent au propriétaire identifié
		- 0 (PAR DEFAUT) si non
		- 1 si oui mais les paramètres suivants doivent être complétés :
			- onBehalfOfContentOwner 
			- type doit prendre la valeur "video"
			En plus, les paramètres suivants ne doivent pas complétés :
			- videoDefinition
			- videoDimension
			- videoDuration
			- videoLicense
			- videoEmbeddable
			- videoSyndicated
			- videoType
	
	forDeveloper : Booléen qui filtre les vidéos publiés via une application ou un site web de l'utilisateur, identifié comme developpeur. 
		- 0 (PAR DEFAUT) si non 
		- 1 si oui
	
	forMine : Filtre les vidéos qui appartienne à l'utilsateur de l'API. 
		- 0 (PAR DEFAUT) si non.
		- 1 si oui mais :
			- type doit prendre la valeur "video"
			- les paramètres suivants ne doivent pas complétés :
				- videoDefinition
				- videoDimension
				- videoDuration
				- videoLicense
				- videoEmbeddable
				- videoSyndicated
				- videoType
	
	relatedToVideoId : ID qui filtre les videos relatifs à celui-ci. Si ce paramètre est complété : 
		- type doit prendre la valeur "video"
		- les seules paramètres acceptés sont:
				- part
				- maxResults
				- pageToken
				- regionCode
				- relevanceLanguage
				- safeSearch
				- type qui doit prendre la valeur "video"
				- fields

PARAMETRES OPTIONELS :
	channelID : ID qui identifie la chaine ou l'auteur. 
		-> Le résultat donne 500 videos max si : 
			- type = "video" 
			- channelId est complété
			- forContentOwner = 0
			- forDeveloper = 0
			- forMine = 0
	
	channelType : Recherche selon un type de chaine :
		- "any" : Toutes les chaines (PAR DEFAUT)
		- "show": Seulement les "shows"?
	
	eventType : Recherche selon le type de diffusion de la vidéo :
		- "completed" : vidéo normal (PAR DEFAUT)
		- "live" : 		diffusion en direct
		- "upcoming" : 	vidéo à venir
	/!\ type doit prendre la valeur "video"
	
	location : En complement de locationRadius, spécifie le centre du cercle de recherche.
		ex: (37.4307, -122.08427)
	
	location : En complement de location, spécifie le rayon de recherche. La valeur est suivi de m, km, ft ou mi. Ex: 1500m, 5km, 10000ft, 0.75mi.
	
	maxResults: nombre max de resultats: Vaut entre 0 et 50. Vaut 5 par défaut.

	onBehalfOfContentOwner: NE PAS EN PRENDRE COMPTE. 

	order : String qui ordonne la liste résultat selon :
		- "date" : par date du plus récent au plus vieux.
		- "rating" : par le ratio Like/Dislike du plus haut au plus bas
		- "relevance" (PAR DEFAUT) : les plus pertinents
		- "title" : ordre alphabetique des titres des videos
		- "videoCount" : nombre de videos de l'auteur dans l'ordre décroissant
		- "viewCount" : nombre de vues decroissant

	pageToken : n° de page du resultats

	publishedAfter : Affiche les videos publié après la date spécifié sous le format :
		YYYY-DD-MMTHH:mm:SSZ (ex: 1970-05-12T05:45:00Z)

	publishedBefore : Affiche les videos publié avant la date spécifié sous le format :
		YYYY-DD-MMTHH:mm:SSZ (ex: 1970-05-12T05:45:00Z)

	q : termes de la recherche

	regionCode : string qui affiche les vidéos selon l'ISO 3166-1 alpha2 du pays

	relevanceLanguage : string qui affiche les vidéos selon la langue: ISO 639-1 two-letter language code

	safeSearch : affiche les vidéos selon leur restriction
		- "moderate" : liste ne contenant pas de vidéo restreint à votre localisation
		- "none" (PAR DEFAUT) : aucun filtre
		- "strict" : liste ne contenant aucune vidéos restreint 

	topicId : Vidéo par catégorie (Mis à jour le 15 février 2017)
	voir https://developers.google.com/youtube/v3/docs/search/list?hl=fr#

	type: type de recherche
		- "channel"
		- "playlist"
		- "video"

	videoCaption : présence de sous-titres
		- "any"	(PAR DEFAUT) : aucun filtre
		- "closedCaption" : vidéo contenant des sous-titres
		- "none" : vidéo contenant aucun sous-titres

	videoCategoryId : Catégorie de la vidéo. Type doit valoir "video". 

	videoDefinition : Qualité de la vidéo
		- "any" (PAR DEFAUT)
		- "high"
		- "standard"

	videoDimension : Dimension de la video
		- "2d" 
		- "3d"
		- "any" (PAR DEFAUT)

	videoDuration : Durée de la vidéo
		- "any" : aucun filtre (PAR DEFAUT)
		- "long" : plus de 20 min
		- "medium" : entre 4 et 20
		- "short" : moins de 4 min

	videoEmbeddable : vidéo pouvant être incorporé dans une page Web
		- "any"
		- "true"

	videoLicense : niveau de license de la vidéo
		- "any" : aucune protection
		- "creativeCommon" : libre
		- "youtube" : license youtube

	videoSyndicated : jouable en dehors du site youtube.com
		- "any" : 
		- "true" : 

	videoType : type particulier de video 
		- "any"
		- "episode"
		- "movie"