from flask import * 
from database import *
import uuid
from datetime import datetime,date


OrphanageManager= Blueprint('OrphanageManager',__name__)

@OrphanageManager.route("/OrphanageHome")
def OrphanageHome():
	return render_template("OrphanageHome.html")

@OrphanageManager.route("/OrphanageOrphanDetails",methods=['get','post'])
def OrphanageOrphanDetails():
	if 'OrphanageOrphanDetails' in request.form:
		fin=request.form['fn']
		lan=request.form['ln']
		dob=request.form['db']
		# ig=request.files['ig']
		# path="static/"+str(uuid.uuid4())+ig.filename
		# ig.save(path)
		age=request.form['age']
		gen=request.form['gd']
		des=request.form['ds']
		q="insert into orphans values(null,'%s','%s','%s','%s','%s','%s','%s')"%(session['lid'],fin,lan,dob,age,gen,des)
		insert(q)
		return redirect(url_for('OrphanageManager.OrphanageOrphanDetails'))

	data={}

	q="select * from orphans"
	res=select(q)
	data['or']=res


	if "search" in request.form:
		sn=request.form['sn']+"%"
		q="select * from `orphans` where `first_name` like '%s' "%(sn)
		print(q)
		data['search']=select(q)



	if 'action' in request.args:
		action=request.args['action']
		oid=request.args['oid']
	else:
		action=None


	if action=="delete":
		q="delete from orphans where orphan_id='%s'"%(oid)
		delete(q)
		return redirect(url_for('OrphanageManager.OrphanageOrphanDetails'))

	if action=="update":
		q="select * from orphans where orphan_id='%s'"%(oid)
		res=select(q)
		data['updates']=res



	if 'update' in request.form:
		fin=request.form['fn']
		lan=request.form['ln']
		dob=request.form['db']
		# ig=request.files['ig']
		# path="static/"+str(uuid.uuid4())+ig.filename
		age=request.form['age']
		gen=request.form['gd']
		des=request.form['ds']
		q="update  orphans set first_name='%s',last_name='%s',dob='%s',gender='%s',about_description='%s',orphan_image='%s' where orphan_id='%s'"%(fin,lan,dob,gen,des,age,oid)
		update(q)
		return redirect(url_for('OrphanageManager.OrphanageOrphanDetails'))

		
	return render_template("OrphanageOrphanDetails.html",data=data)

@OrphanageManager.route("/OrphanageRequirements",methods=['get','post'])
def OrphanageRequirements():
	data={}
	if 'OrphanageRequirements' in request.form:
		des=request.form['ds']
		q="insert into requirements values(null,'%s','%s',now(),'pending')"%(session['lid'],des)
		insert(q)
		return redirect(url_for('OrphanageManager.OrphanageRequirements'))
	q="select * from requirements"
	res=select(q)
	data['or']=res

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None


	if action=="delete":
		q="delete from requirements where requirement_id='%s'"%(rid)
		delete(q)
		return redirect(url_for('OrphanageManager.OrphanageRequirements'))
	return render_template("OrphanageRequirements.html",data=data)




@OrphanageManager.route("/OrphanageViewAdoptionRequest")
def OrphanageViewAdoptionRequest():
	data={}
	q="SELECT * ,CONCAT(user.first_name,' ', user.last_name)AS uname, CONCAT(orphans.first_name,' ',orphans.last_name) AS oname FROM adoption_request INNER JOIN USER USING (user_id) INNER JOIN orphans USING(orphan_id)"
	res=select(q)
	data['or']=res

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
	else:
		action=None


	if action=="deny":
		q="delete from adoption_request where adoption_request_id='%s'"%(aid)
		delete(q)
		return redirect(url_for('OrphanageManager.OrphanageViewAdoptionRequest'))

	if action=="accept":
		q="update  adoption_request set status='accept' where adoption_request_id='%s'"%(aid)
		update(q)
		return redirect(url_for('OrphanageManager.OrphanageViewAdoptionRequest'))





	return render_template("OrphanageViewAdoptionRequest.html",data=data)

@OrphanageManager.route("/OrphanageSponsorRequests")
def OrphanageSponsorRequests():
	data={}
	q="SELECT * ,CONCAT(user.first_name,' ', user.last_name)AS uname, CONCAT(orphans.first_name,' ',orphans.last_name) AS oname FROM sponsor_requests INNER JOIN USER USING (user_id) INNER JOIN orphans USING(orphan_id)"
	res=select(q)
	data['or']=res



	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None


	if action=="deny":
		q="delete from sponsor_requests where sponsor_req_id='%s'"%(sid)
		delete(q)
		return redirect(url_for('OrphanageManager.OrphanageSponsorRequests'))

	if action=="accept":
		q="update  sponsor_requests set status='accept' where sponsor_req_id='%s'"%(sid)
		update(q)
		return redirect(url_for('OrphanageManager.OrphanageSponsorRequests'))

	return render_template("OrphanageSponsorRequests.html",data=data)

@OrphanageManager.route("/AddDonation")
def AddDonation():
	data={}
	q="SELECT * from donations inner join user using(user_id) "

	res=select(q)
	data['view']=res
	return render_template("AddDonation.html",data=data)

@OrphanageManager.route("/OrphanageViewTeachingRequests")
def OrphanageViewTeachingRequests():
	data={}

	q="SELECT *,CONCAT(user.first_name,' ',user.last_name) AS uname FROM `teaching_requests` INNER JOIN `user` USING (`user_id`)"
	res=select(q)
	data['or']=res
	if 'action' in request.args:
		action=request.args['action']
		tid=request.args['tid']
	else:
		action=None


	if action=="deny":
		q="delete from teaching_requests where teaching_req_id='%s'"%(tid)
		delete(q)
		return redirect(url_for('OrphanageManager.OrphanageViewTeachingRequests'))

	if action=="accept":
		q="update  teaching_requests set status='accept' where teaching_req_id='%s'"%(tid)
		update(q)
		return redirect(url_for('OrphanageManager.OrphanageViewTeachingRequests'))


	return render_template("OrphanageViewTeachingRequests.html",data=data)

# @OrphanageManager.route("/home")
# def home():
# 	return render_template("home.html")

@OrphanageManager.route('/eventssss',methods=['get','post'])
def eventssss():
	data={}

	print("hiiiiiiiiiiii")

	if 'event' in request.form:
		evn=request.form['et']
		ven=request.form['vn']
		dat=request.form['dt']
		chg=request.form['cg']
		des=request.form['ds']
		q="insert into event values(null,'%s','%s','%s','%s','%s','event added')"%(evn,ven,dat,chg,des)
		insert(q)
		print(q)
		return redirect(url_for('OrphanageManager.eventssss'))
	q="select * from event"
	res=select(q)
	print(res)
	data['or']=res

	print("hiiiiiiiiiiii")


	if 'action' in request.args:
		action=request.args['action']
		event_id=request.args['event_id']

	else:
		action=None
	print("kkkkkkkkkkkkkkk",action)

	if action=="delete":
		print("vvvvvvvvvvvvv")

		q="delete from event where event_id='%s'"%(event_id)
		delete(q)
		print(q)
		return redirect(url_for('OrphanageManager.eventssss'))


	return render_template("eventssss.html",data=data)

@OrphanageManager.route("/AdminViewOrphans")
def AdminViewOrphans():
	data={}

	q="select * from orphans"
	res=select(q)
	data['or']=res
	return render_template("AdminViewOrphans.html",data=data)

@OrphanageManager.route('/orphanageviewusers')
def orphanageviewusers():
	data={}

	q="select * from user"
	res=select(q)
	data['or']=res
	return render_template("orphanageviewusers.html",data=data)

@OrphanageManager.route('/AdminViewTestimonials')
def AdminViewTestimonials():
	data={}

	q="SELECT * FROM feedback INNER JOIN `user` on user.login_id=feedback.user_id"
	res=select(q)
	data['or']=res
	return render_template("AdminViewTestimonials.html",data=data)







@OrphanageManager.route('/printorphans',methods=['get','post'])
def printorphans():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM  orphans"
	r=select(q)
	data['view']=r
	
	return render_template('printorphans.html',data=data)



@OrphanageManager.route('/printrequirement',methods=['get','post'])
def printrequirement():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM  requirements"
	r=select(q)
	data['view']=r
	
	return render_template('printrequirement.html',data=data)



@OrphanageManager.route('/printcharity',methods=['get','post'])
def printcharity():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM  EVENT"
	r=select(q)
	data['view']=r
	
	return render_template('printcharity.html',data=data)



@OrphanageManager.route('/printuser',methods=['get','post'])
def printuser():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM  user"
	r=select(q)
	data['view']=r
	
	return render_template('printuser.html',data=data)




@OrphanageManager.route('/printsponsor',methods=['get','post'])
def printsponsor():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * ,CONCAT(user.first_name,' ', user.last_name)AS uname, CONCAT(orphans.first_name,' ',orphans.last_name) AS oname FROM sponsor_requests INNER JOIN USER USING (user_id) INNER JOIN orphans USING(orphan_id)"
	r=select(q)
	data['view']=r
	
	return render_template('printsponsor.html',data=data)




