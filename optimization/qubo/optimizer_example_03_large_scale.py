import requests
import json
# GET THE CONFIG
import utils

# program
program = """
    minimize(list(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11),
        ((0.00050280851*x1*x1)+(-0.00019062827545936423*x1*x2)+(-4.031530205846567e-05*x1*x3)
        +(0.0007700176504322732*x1*x4)+(6.192713992171585e-05*x1*x5)+(0.00048811123386023885*x1*x6)
        +(-0.00023036235438285524*x1*x7)+(-8.794945473561527e-05*x1*x8)+(0.00017771429542756334*x1*x9)
        +(-0.00028016271120196974*x1*x10)+(1.8261617634297466e-05*x1*x11)+(-0.00019062827545936423*x2*x1)
        +(0.0002215961095*x2*x2)+(4.138051815909238e-05*x2*x3)+(-0.00026616938600436315*x2*x4)
        +(-2.6005447507047694e-05*x2*x5)+(-0.00019009026157816382*x2*x6)+(0.00038132936867621534*x2*x7)
        +(9.12582481698027e-05*x2*x8)+(-7.144269058242879e-05*x2*x9)+(0.0003274615890845067*x2*x10)
        +(-6.948233787202782e-06*x2*x11)+(-4.031530205846567e-05*x3*x1)+(4.138051815909238e-05*x3*x2)
        +(1.033340535e-05*x3*x3)+(-6.673337963305604e-05*x3*x4)+(-3.8409998700419695e-07*x3*x5)
        +(-3.770919999804347e-05*x3*x6)+(5.0682785566240185e-05*x3*x7)+(2.149816919905578e-05*x3*x8)
        +(-1.2906774843073148e-05*x3*x9)+(6.069472466996569e-05*x3*x10)+(7.830762370487581e-07*x3*x11)
        +(0.0007700176504322732*x4*x1)+(-0.00026616938600436315*x4*x2)+(-6.673337963305604e-05*x4*x3)
        +(0.001219171765*x4*x4)+(7.562576050701523e-05*x4*x5)+(0.0007380159825363063*x4*x6)
        +(-0.00023041520169260102*x4*x7)+(-0.00014086357313986166*x4*x8)+(0.00026378168779700494*x4*x9)
        +(-0.00038925522235463056*x4*x10)+(1.9545642861722545e-05*x4*x11)+(6.192713992171585e-05*x5*x1)
        +(-2.6005447507047694e-05*x5*x2)+(-3.8409998700419695e-07*x5*x3)+(7.562576050701523e-05*x5*x4)
        +(1.76012048e-05*x5*x5)+(6.476448698375362e-05*x5*x6)+(-7.124303554703252e-05*x5*x7)
        +(-3.260291775633701e-06*x5*x8)+(2.601586810319568e-05*x5*x9)+(-3.910717150957514e-05*x5*x10)
        +(6.701513687147297e-06*x5*x11)+(0.00048811123386023885*x6*x1)+(-0.00019009026157816382*x6*x2)
        +(-3.770919999804347e-05*x6*x3)+(0.0007380159825363063*x6*x4)+(6.476448698375362e-05*x6*x5)
        +(0.000476109129*x6*x6)+(-0.00025094866257730354*x6*x7)+(-8.340248266012542e-05*x6*x8)
        +(0.0001745215178258947*x6*x9)+(-0.0002798260167923604*x6*x10)+(1.977381483915984e-05*x6*x11)
        +(-0.00023036235438285524*x7*x1)+(0.00038132936867621534*x7*x2)+(5.0682785566240185e-05*x7*x3)
        +(-0.00023041520169260102*x7*x4)+(-7.124303554703252e-05*x7*x5)+(-0.00025094866257730354*x7*x6)
        +(0.0008289611*x7*x7)+(0.00012168529988102242*x7*x8)+(-0.00010491538277051133*x7*x9)
        +(0.0005672198584384658*x7*x10)+(-2.540282805646928e-05*x7*x11)+(-8.794945473561527e-05*x8*x1)
        +(9.12582481698027e-05*x8*x2)+(2.149816919905578e-05*x8*x3)+(-0.00014086357313986166*x8*x4)
        +(-3.260291775633701e-06*x8*x5)+(-8.340248266012542e-05*x8*x6)+(0.00012168529988102242*x8*x7)
        +(4.5209583e-05*x8*x8)+(-2.91667702333832e-05*x8*x9)+(0.00013407502626712708*x8*x10)
        +(6.297422691107892e-07*x8*x11)+(0.00017771429542756334*x9*x1)+(-7.144269058242879e-05*x9*x2)
        +(-1.2906774843073148e-05*x9*x3)+(0.00026378168779700494*x9*x4)+(2.601586810319568e-05*x9*x5)
        +(0.0001745215178258947*x9*x6)+(-0.00010491538277051133*x9*x7)+(-2.91667702333832e-05*x9*x8)
        +(6.45818595e-05*x9*x9)+(-0.00010539697220660459*x9*x10)+(8.274801681695728e-06*x9*x11)
        +(-0.00028016271120196974*x10*x1)+(0.0003274615890845067*x10*x2)+(6.069472466996569e-05*x10*x3)
        +(-0.00038925522235463056*x10*x4)+(-3.910717150957514e-05*x10*x5)+(-0.0002798260167923604*x10*x6)
        +(0.0005672198584384658*x10*x7)+(0.00013407502626712708*x10*x8)+(-0.00010539697220660459*x10*x9)
        +(0.00048398427750000005*x10*x10)+(-1.0596258285851005e-05*x10*x11)+(1.8261617634297466e-05*x11*x1)
        +(-6.948233787202782e-06*x11*x2)+(7.830762370487581e-07*x11*x3)+(1.9545642861722545e-05*x11*x4)
        +(6.701513687147297e-06*x11*x5)+(1.977381483915984e-05*x11*x6)+(-2.540282805646928e-05*x11*x7)
        +(6.297422691107892e-07*x11*x8)+(8.274801681695728e-06*x11*x9)+(-1.0596258285851005e-05*x11*x10)
        +(2.6589402100000005e-06*x11*x11)-((-0.01*x1)+(-0.0185*x2)+(-0.0115*x3)+(-0.007*x4)
        +(-0.0225*x5)+(-0.0115*x6)+(-0.006*x7)+(-0.0115*x8)+(-0.006*x9)+(-0.017*x10)+(-0.02*x11)))) 
        & label('total', x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11==@1) 
        & label('eqlimit', (0.0*x1)+(0.0*x2)+(0.0*x3)+(0.0*x4)+(3.3333333333333335*x5)+(0.0*x6)+(0.0*x7)+(3.3333333333333335*x8)+(0.0*x9)+(3.3333333333333335*x10)+(3.3333333333333335*x11)<@1) 
        & label('filimit', (2.0*x1)+(2.0*x2)+(0.0*x3)+(0.0*x4)+(0.0*x5)+(2.0*x6)+(0.0*x7)+(0.0*x8)+(0.0*x9)+(0.0*x10)+(0.0*x11)<@1) 
        & label('xxxlimit', (0.0*x1)+(0.0*x2)+(2.0*x3)+(2.0*x4)+(0.0*x5)+(0.0*x6)+(2.0*x7)+(0.0*x8)+(0.0*x9)+(0.0*x10)+(0.0*x11)<@1)
""".replace("\n", "").replace("\r", "")
print("program = " , program)
# vars
vars = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11']
# weights
weights = {'total': 100.0, 'eqlimit': 100.0, 'filimit': 100.0, 'xxxlimit': 100.0}

user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

config = {"configSelect":"JuliaConfig"}
target = program 
symbols = vars
weights = weights

url = "https://api2.anzaetek.com:443/execute"

def query_optimizer(config, target, symbols, weights):
    q = { 
        "__class__":"SolverProblem", 
        "query":{ "Description":{"Terms":[],"ForceNBits":[],"Parameters":{},"Initialization":{}},
                "DescriptionString":target,
                "DescriptionSymbolList":symbols,
                "DescriptionParameters":weights,
                "Config":config,
                "Info":{"user":user1,"token":token1}}}
    query = {'user': user1, 
            'token': token1, 
            'query': json.dumps(q)}
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    return { k: rv['Results'][k] for k in symbols }

v = query_optimizer(config, target, symbols, weights)
print(v)