def reverse_msg(message):
	return message[::-1]

def reverse_with_arr(message):
	reversedString=[]
	index = len(message)
	while index > 0: 
	    reversedString += message[ index - 1 ]
	    index = index - 1
	return ''.join(reversedString)

def reverse_optimized(message):
	start = 0
	end = len(message)-1
	message = list(message)
	while start < end:
		message[start], message[end] = message[end], message[start]
		start += 1
		end -= 1

	return ''.join(message)

message = "Hello world"
print( reverse_msg(message) )
print( reverse_with_arr(message) )
print( reverse_optimized(message) )