def bob(text):
  punct=[".","?","!"," "]
  letters=[]
  for i in range(0, len(text)):
  	if text[i] in punct:
  		letter=""
  	else:
  		letter=text[i]
  	letters.append(letter)
  	
  simple_text = "".join(letters)
  
  if simple_text== "Bob":
  	return "Fine. Be that way!"
  
  if text == text.upper():
  	return "Whoa, chill out!"
  
  elif text[len(text)-1] == "?":	
    return "Sure."
  
  else:
  	return "Whatever."
  	
