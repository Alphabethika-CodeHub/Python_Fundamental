print("Python Operators Reference: https://www.w3schools.com/python/python_operators.asp")

print("""
Python Divides The Operators in The Following Groups :
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators
""")

print("""
Python Arithmetic Operators :
---------------------------------------------
Operator	    Name	            Example
---------------------------------------------
+	            Addition	        x + y
-	            Subtraction	        x - y
*	            Multiplication	    x * y
/	            Division	        x / y
%	            Modulus	            x % y
**	            Exponentiation	    x ** y
//	            Floor division	    x // y
""")

print("""
Python Assignment Operators :
------------------------------------------
Operator	Example	        Same As
------------------------------------------	
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)	x = 3
                            print(x)
""")

print("""
Python Comparison Operators :
------------------------------------------------------
Operator	    Name	                    Example
------------------------------------------------------
==	            Equal	                    x == y	
!=	            Not equal	                x != y	
>	            Greater than	            x > y	
<	            Less than	                x < y	
>=	            Greater than or equal to	x >= y	
<=	            Less than or equal to	    x <= y
""")

print("""
Python Logical Operators :
----------------------------------------------------------------------------------------------
Operator	Description	                                                Example
----------------------------------------------------------------------------------------------
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true     not(x < 5 and x < 10)
""")

print("""
Python Identity Operators :
---------------------------------------------------------------------------------------------- 
Operator	Description	                                                Example
----------------------------------------------------------------------------------------------
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y
""")

print("""
Python Membership Operators :
---------------------------------------------------------------------------------------------------------------
Operator	Description	                                                                            Example
---------------------------------------------------------------------------------------------------------------
in 	        Returns True if a sequence with the specified value is present in the object	        x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y
""")

print("""
Python Bitwise Operators :
---------------------------------------------------------------------------------------------------------------
Operator	Name	                Description                                                     Example
---------------------------------------------------------------------------------------------------------------
& 	        AND	                    Sets each bit to 1 if both bits are 1	                        x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is                        1	x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is                   1	x ^ y	
~	        NOT	                    Inverts all the bits	                                        ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the 
                                    leftmost bits fall off	                                        x << 2	
>>	        Signed right shift	    Shift right by pushing copies of the leftmost 
                                    bit in from the left, and let the rightmost bits fall off	    x >> 2
""")

print("""
Operator Precedence:
-----------------------------------------------------------------------------------
Operator	                Description
-----------------------------------------------------------------------------------
()	                        Parentheses	
**	                        Exponentiation	
+x  -x  ~x	                Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                Multiplication, division, floor division, and modulus	
+  -	                    Addition and subtraction	
<<  >>	                    Bitwise left and right shifts	
&	                        Bitwise AND	
^	                        Bitwise XOR	
|	                        Bitwise OR	
==  !=  >  >=  <  <=  
is  is not  in  not in 	    Comparisons, identity, and membership operators	
not	                        Logical NOT	
and	                        AND	
or	                        OR
""")

