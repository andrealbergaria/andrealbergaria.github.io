
import Math
def compare(s1,s2):
    if s1 == s2:
        return True
    else:
        return False

def length_division(s1):
    len = math.log(s1,0x100)
    retValueRounded = math.floor(len)
    retValueRounded += 1
    return retValueRounded

def length_bitwise_python(s1):
    s_t = int(s1)
    b = s_t.bit_length()
    return b

def concatChar(s1,char):
    str_aux = s1 * 0x100
    str_aux += char
    return str_aux

def concatString(originalString,stringToConcat):
    l = length(stringToConcat)
    num_aux = originalString * math.pow(0x100,l)
    num_aux_floor = math.floor(num_aux)
    num_aux_floor += stringToConcat
    return num_aux_floor

def powerOptimised(a, n):

    # Stores final answer
    ans = 1

    while (n > 0):
        last_bit = (n & 1)

        # Check if current LSB
        # is set
        if (last_bit):
            ans = ans * a
        a = a * a

        # Right shift
        n = n >> 1

    return ans


def getCharAtPosition(originalString,position):
    auxNumber = powerOptimised(0x100,position)
    varAux = math.floor(originalString / auxNumber)
    varResult = varAux % 0x100

    return varResult

def substring_AND(originalString,initial_position,end_position):

    lenOriginalString = length(originalString)
    lenSubstring = end_position - initial_position


    l = 1
    r = (lenSubstring +1) * 8

    mask = (((1 << (l - 1)) - 1) ^
              ((1 << (r)) - 1))

    mask <<= initial_position*8

    substring = originalString & mask
    substring >>= initial_position * 8


    return substring


def setSubstring(originalString,substring,initialPosition,endPosition):
    lenSubstring =  endPosition-initialPosition #len for bytes..convert to bin (*8)

    if length(substring) != lenSubstring:
        print("Wrong, substring different from end_position - initial_position")
        return

    maskOr = substring << initialPosition*8

    lenSubstringInBits   = lenSubstring *8
    mask = (1 << lenSubstringInBits) - 1

    shiftToBeginPosition = mask << initialPosition*8


    aux = originalString & shiftToBeginPosition
    xor_result = aux ^ originalString
    result_or = xor_result | maskOr

def trailing_zeros(x):
    return (x & -x).bit_length() - 1


