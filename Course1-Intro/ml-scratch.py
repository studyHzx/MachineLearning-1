import graphlab
sa = graphlab.SArray(wordcount.keys())


wordcount = {'and': 3,  'bags': 1,  'came': 1, 'disappointed.': 1, 'does': 1, 'early': 1, 'highly': 1, 'holder.': 1, 'i': 1, 'it': 2, 'it.': 1, 'keps': 1, 'leak.': 1, 'love': 1, 'moist': 1, 'my': 2, 'not': 2, 'now': 1, 'osocozy': 1, 'planet': 1, 'recommend': 1, 'was': 1, 'wipe': 1, 'wipes': 1, 'wise': 1}
selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']


def selDict (key, aDict):	
	if (key in selected_words):
		return (key, aDict.get(key))
}