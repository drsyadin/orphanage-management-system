from flask import * 
from database import *

user= Blueprint('user',__name__)

@user.route("/UserHome")
def UserHome():
	return render_template("UserHome.html")


@user.route("/UserViewOrphans")
def UserViewOrphans():
	data={}

	q="select * from orphans"
	res=select(q)
	data['or']=res
	return render_template("UserViewOrphans.html",data=data)

@user.route("/SendTeachingInterest",methods=['get','post'])
def SendTeachingInterest():
	if 'SendTeachingInterest' in request.form:
		ds=request.form['des']
		q="insert into teaching_requests values(null,'%s','%s',now(),'pending')"%(session['user_id'],ds)
		insert(q)
	return render_template("SendTeachingInterest.html")

@user.route("/SendAdoptionRequest",methods=['get','post'])
def SendAdoptionRequest():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='filter':
		kj="select * from orphans where orphan_image <='%s'"%(cid)
		print(kj)
		data['view']=select(kj)
	else:
		kj="select * from orphans "
		data['view']=select(kj)		
	if 'SendAdoptionRequest' in request.form:
		ds=request.form['des']
		org=request.form['org']
		q="insert into adoption_request values(null,'%s','%s','%s',now(),'pending')"%(session['user_id'],org,ds)
		insert(q)
	return render_template("SendAdoptionRequest.html",data=data)


@user.route('/UserViewRequirements',methods=['get','post'])
def UserViewRequirements():
	data={}
	
	q="SELECT * FROM `requirements` where status !='donated'"
	res=select(q)
	data['or']=res


	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None


	if action=="deny":

		q="delete from requirements where requirement_id='%s'"%(sid)
		delete(q)
		return redirect(url_for('user.UserViewRequirements'))

	if action=="accept":
	
		q="update  requirements set status='accept' where requirement_id='%s'"%(sid)
		update(q)
		return redirect(url_for('user.UserViewRequirements'))
	return render_template("UserViewRequirements.html",data=data)

@user.route("/SendDonation",methods=['get','post'])
def SendDonation():
	if 'SendDonation' in request.form:
		requirement_id=request.args['requirement_id']
		at=request.form['amt']
		q="insert into donations values(null,'%s','%s','%s',now())"%(session['user_id'],requirement_id,at)
		insert(q)
		q="update  requirements set status='donated' where requirement_id='%s'"%(requirement_id)
		update(q)
		return redirect(url_for('user.UserHome'))
	return render_template("SendDonation.html")

@user.route("/SponsorOrphan",methods=['get','post'])
def SponsorOrphan():
	if 'SponsorOrphan' in request.form:
		cod=request.form['cd']
		orphan_id=request.args['orphan_id']
		q="insert into sponsor_requests values(null,'%s','%s','%s',now(),'pending')"%(session['user_id'],orphan_id,cod)
		insert(q)
	return render_template("SponsorOrphan.html")

@user.route("/UserAddTestimonials",methods=['get','post'])
def UserAddTestimonials():
	data={}
	if 'UserAddTestimonials' in request.form:
		des=request.form['ds']
		q="insert into feedback values(null,'%s','%s',now())"%(session['lid'],des)
		insert(q)
		return redirect(url_for('user.UserAddTestimonials'))
	q="select * from feedback where user_id='%s'"%(session['lid'])
	res=select(q)
	data['or']=res
	return render_template("UserAddTestimonials.html",data=data)

@user.route("/UserViewMyAdoptionRequest")
def UserViewMyAdoptionRequest():
	data={}
	q="select * from adoption_request where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['or']=res
	return render_template("UserViewMyAdoptionRequest.html",data=data)

@user.route("/UserViewMySponsorRequest")
def UserViewMySponsorRequest():
	data={}
	q="select * from sponsor_requests where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['or']=res
	return render_template("UserViewMySponsorRequest.html",data=data)

@user.route("/UserViewMyTeachingRequest")
def UserViewMyTeachingRequest():
	data={}
	q="select * from teaching_requests where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['or']=res
	return render_template("UserViewMyTeachingRequest.html",data=data)

@user.route("/UserViewEvent")
def UserViewEvent():
	data={}
	q="select * from event"
	res=select(q)
	data['or']=res
	return render_template("UserViewEvent.html",data=data)