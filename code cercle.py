Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> import json
>>> r=float(input('Rayon:'))
Rayon:30
>>> i=0
>>> while i<50:
	x=r*math.cos((i*2*math.pi)/50)-r
	y=r*math.sin((i*2*math.pi)/50)
	z=0
	coordonnees=[x,y,z]
	json.dumps(coordonnees)
	i=i+1

'[0.0, 0.0, 0]'
'[-0.23655896056566306, 3.7599970069291277, 0]'
'[-0.9425051661410677, 7.460696614945644, 0]'
'[-2.106705423352455, 11.043736580540337, 0]'
'[-3.710799598684094, 14.45261022305146, 0]'
'[-5.729490168751575, 17.633557568774194, 0]'
'[-8.130941177357652, 20.53641317786066, 0]'
'[-10.877280307539309, 23.115397283273676, 0]'
'[-13.925196150630104, 25.329837765060454, 0]'
'[-17.22662125304782, 27.144811573980586, 0]'
'[-20.729490168751575, 28.531695488854606, 0]'
'[-24.37856056242826, 29.468617521860658, 0]'
'[-28.116284414120592, 29.940801852848146, 0]'
'[-31.8837155858794, 29.940801852848146, 0]'
'[-35.62143943757174, 29.46861752186066, 0]'
'[-39.27050983124841, 28.53169548885461, 0]'
'[-42.77337874695218, 27.144811573980583, 0]'
'[-46.07480384936991, 25.32983776506045, 0]'
'[-49.12271969246069, 23.115397283273676, 0]'
'[-51.869058822642344, 20.536413177860666, 0]'
'[-54.27050983124842, 17.633557568774197, 0]'
'[-56.28920040131591, 14.452610223051456, 0]'
'[-57.89329457664754, 11.043736580540344, 0]'
'[-59.057494833858925, 7.4606966149456575, 0]'
'[-59.76344103943433, 3.759997006929136, 0]'
'[-60.0, 3.67394039744206e-15, 0]'
'[-59.76344103943434, -3.7599970069291286, 0]'
'[-59.05749483385894, -7.460696614945637, 0]'
'[-57.89329457664755, -11.043736580540337, 0]'
'[-56.2892004013159, -14.452610223051462, 0]'
'[-54.27050983124843, -17.63355756877418, 0]'
'[-51.86905882264235, -20.536413177860652, 0]'
'[-49.122719692460684, -23.11539728327368, 0]'
'[-46.074803849369886, -25.32983776506046, 0]'
'[-42.77337874695216, -27.144811573980594, 0]'
'[-39.270509831248425, -28.531695488854606, 0]'
'[-35.62143943757174, -29.46861752186066, 0]'
'[-31.883715585879397, -29.940801852848146, 0]'
'[-28.116284414120614, -29.940801852848146, 0]'
'[-24.378560562428273, -29.46861752186066, 0]'
'[-20.729490168751582, -28.53169548885461, 0]'
'[-17.226621253047846, -27.144811573980597, 0]'
'[-13.925196150630097, -25.32983776506045, 0]'
'[-10.877280307539323, -23.115397283273687, 0]'
'[-8.130941177357663, -20.53641317786067, 0]'
'[-5.729490168751578, -17.6335575687742, 0]'
'[-3.7107995986841047, -14.452610223051483, 0]'
'[-2.106705423352455, -11.043736580540337, 0]'
'[-0.9425051661410713, -7.46069661494566, 0]'
'[-0.2365589605656666, -3.7599970069291393, 0]'
>>> 
