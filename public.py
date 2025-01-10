from flask import * 
from database import *

public= Blueprint('public',__name__)

@public.route('/')
def index():
	return render_template("index.html")


@public.route('/login',methods=['get','post'])
def login():
	if 'login' in request.form:
		u=request.form['names']
		p=request.form['pwd']
		print(u,p)
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q);
		if res:
			session['lid']=res[0]['log_id']
			if res[0]['type']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['type']=="orphanage":
				q1="select * from orphanage where login_id='%s'"%(session['lid'])
				res1=select(q1)
				if res1:
					session['orphanage_id']=res1[0]['orphanage_id']
					return redirect(url_for('OrphanageManager.OrphanageHome'))
			elif res[0]['type']=="user":
				q1="select * from user where login_id='%s'"%(session['lid'])
				res1=select(q1)
				if res1:
					session['user_id']=res1[0]['user_id']
					return redirect(url_for('user.UserHome'))



			
			
	return render_template("login.html")

# @public.route('/registration',methods=['get','post'])
# def registration():
# 	if 'registration' in request.form:
# 		n=request.form['nam']
# 		ad=request.form['abc']
# 		phno=request.form['ph']
# 		e=request.form['email']
# 		d=request.form['dt']
# 		print(n,ad,phno,e,d)
# 	return render_template("registration.html")

@public.route('/orphanageRegistration',methods=['get','post'])
def orphanageRegistration():
	if 'orphanageRegistration' in request.form:
		on=request.form['names']
		pl=request.form['pla']
		pc=request.form['pin']
		di=request.form['dis']
		ph=request.form['ph']
		em=request.form['mail']
		ac=request.form['adcr']
		sc=request.form['spcr']
		# print(on,pl,pc,di,ph,em,ac,sc)
		u=request.form['names']
		p=request.form['pwd']
		q="insert into login values(null,'%s','%s','orphanage')"%(u,p)
		id=insert(q)
		q="insert into orphanage values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,on,pl,pc,di,ph,em,ac,sc)
		insert(q)
	return render_template("orphanageRegistration.html")

@public.route('/userRegistration',methods=['get','post'])
def userRegistration():
	if 'userRegistration' in request.form:
		fnm=request.form['fn']
		lnm=request.form['ln']
		gd=request.form['gen']
		hn=request.form['hname']
		pla=request.form['pl']
		pn=request.form['pho']
		em=request.form['eml']
		oc=request.form['occu']
#		print(fnm,lnm,gd,hn,pla,pn,em,oc)
		u=request.form['names']
		p=request.form['pwd']
		q="insert into login values(null,'%s','%s','user')"%(u,p)
		id=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fnm,lnm,gd,hn,pla,pn,em,oc)
		insert(q)
	return render_template("userRegistration.html")


@public.route('/PublicViewRequirements')
def PublicViewRequirements():
	data={}
	
	q="SELECT * FROM `requirements` INNER JOIN `orphanage` USING (`orphanage_id`)"
	res=select(q)
	data['or']=res
	return render_template("PublicViewRequirements.html",data=data)

@public.route('/PublicViewFeedback')
def PublicViewFeedback():
	data={}

	q="SELECT * FROM feedback INNER JOIN `orphanage` USING (`orphanage_id`)"
	res=select(q)
	data['or']=res
	return render_template("PublicViewFeedback.html",data=data)

@public.route("/PublicViewEvent")
def PublicViewEvent():
	data={}
	q="select * from event"
	res=select(q)
	data['or']=res
	return render_template("PublicViewEvent.html",data=data)


@public.route('/publicorphanage')
def publicorphanage():
	data={}

	q="select * from orphanage"
	res=select(q)
	data['or']=res


	return render_template("publicorphanage.html",data=data)
@public.route('/publicrequirement')
def publicrequirement():
	data={}
	
	q="SELECT * FROM `requirements` INNER JOIN `orphanage` USING (`orphanage_id`)"
	res=select(q)
	data['or']=res
	return render_template("publicrequirement.html",data=data)


@public.route('/publictestimonials')
def publictestimonials():
	data={}

	q="select * from feedback "
	res=select(q)
	data['or']=res
	return render_template("publictestimonials.html",data=data)