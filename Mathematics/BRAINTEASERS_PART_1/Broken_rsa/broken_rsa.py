from Crypto.Util.number import inverse, long_to_bytes
from math import gcd
n = 27772857409875257529415990911214211975844307184430241451899407838750503024323367895540981606586709985980003435082116995888017731426634845808624796292507989171497629109450825818587383112280639037484593490692935998202437639626747133650990603333094513531505209954273004473567193235535061942991750932725808679249964667090723480397916715320876867803719301313440005075056481203859010490836599717523664197112053206745235908610484907715210436413015546671034478367679465233737115549451849810421017181842615880836253875862101545582922437858358265964489786463923280312860843031914516061327752183283528015684588796400861331354873
e = 16
c = 11303174761894431146735697569489134747234975144162172162401674567273034831391936916397234068346115459134602443963604063679379285919302225719050193590179240191429612072131629779948379821039610415099784351073443218911356328815458050694493726951231241096695626477586428880220528001269746547018741237131741255022371957489462380305100634600499204435763201371188769446054925748151987175656677342779043435047048130599123081581036362712208692748034620245590448762406543804069935873123161582756799517226666835316588896306926659321054276507714414876684738121421124177324568084533020088172040422767194971217814466953837590498718

def prime_mod_sqrt(a, p):

    """
    Square root modulo prime number
    Solve the equation
        x^2 = a mod p
    and return list of x solution
    """
    a %= p

    # Simple case
    if a == 0:
        return [0]
    if p == 2:
        return [a]

    # Check solution existence on odd prime
    if legendre_symbol(a, p) != 1:
        return []

    # Simple case
    if p % 4 == 3:
        x = pow(a, (p + 1)//4, p)
        return [x, p-x]

    # Factor p-1 on the form q * 2^s (with Q odd)
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2

    # Select a z which is a quadratic non resudue modulo p
    z = 1
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    # Search for a solution
    x = pow(a, (q + 1)//2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        # Find the lowest i such that t^(2^i) = 1
        i, e = 0, 2
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        # Update next value to iterate
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]

def legendre_symbol(a, p):
    ls = pow(a, (p - 1)//2, p)
    return -1 if ls==p-1 else ls
      
res=[c]
cnt=0
while len(res) < 32:
	res+=prime_mod_sqrt(res[cnt], n)
	cnt+=1
	print(cnt,res,len(res))

for i in res:
	if b'crypto{' in long_to_bytes(i):
		print(i)
		print(long_to_bytes(i))

s=3539237778217166137842555505989117928829373135679837081419793629975084339895165734744802166985243124825558545835111376731639963926630733027020121729222875979138253687409199990746840367239948177008792432240913040959783652482774028474930018387772452212315504588656134688759198795637320603697276380147029386127517034728685287241008264454039149966809075617511786899506397040329859490325408881358346677488650021265701441002763289567009616142451526468236858947361753824473530778652420098975754873762941
for i in range(len(res)):
	if res[i] == s: print(i)



