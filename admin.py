from flask import * 
from database import *

admin= Blueprint('admin',__name__)

@admin.route("/adminhome")
def adminhome():
	return render_template("adminhome.html")

@admin.route('/AdminViewOrphanage')
def AdminViewOrphanage():
	data={}

	q="select * from orphanage"
	res=select(q)
	data['or']=res


	return render_template("AdminViewOrphanage.html",data=data)

@admin.route("/AdminViewOrphans")
def AdminViewOrphans():
	data={}

	q="select * from orphans"
	res=select(q)
	data['or']=res
	return render_template("AdminViewOrphans.html",data=data)

	
@admin.route("/home")
def home():
	return render_template("home.html")

@admin.route('/event',methods=['get','post'])
def event():
	data={}
	if 'event' in request.form:
		evn=request.form['et']
		ven=request.form['vn']
		dat=request.form['dt']
		chg=request.form['cg']
		des=request.form['ds']
		q="insert into event values(null,'%s','%s','%s','%s','%s','event added')"%(evn,ven,dat,chg,des)
		insert(q)
	q="select * from event"
	res=select(q)
	data['or']=res
	return render_template("event.html",data=data)

@admin.route('/AdminViewRequirements')
def AdminViewRequirements():
	data={}
	
	q="SELECT * FROM `requirements` INNER JOIN `orphanage` USING (`orphanage_id`)"
	res=select(q)
	data['or']=res
	return render_template("AdminViewRequirements.html",data=data)

@admin.route('/AdminViewUsers')
def AdminViewUsers():
	data={}

	q="select * from user"
	res=select(q)
	data['or']=res
	return render_template("AdminViewUsers.html",data=data)
	
@admin.route('/AdminViewAdoptionRequests')
def AdminViewAdoptionRequests():
	data={}

	q="SELECT * ,CONCAT(user.first_name,' ', user.last_name)AS uname, CONCAT(orphans.first_name,' ',orphans.last_name) AS oname FROM adoption_request INNER JOIN USER USING (user_id) INNER JOIN orphans USING(orphan_id)"
	res=select(q)
	data['or']=res
	return render_template("AdminViewAdoptionRequests.html",data=data)


@admin.route('/AdminViewDonations')
def AdminViewDonations():
	data={}

	q="SELECT *,CONCAT(user.first_name,' ',user.last_name) AS uname FROM donations INNER JOIN `user` USING (`user_id`)"
	res=select(q)
	data['or']=res
	return render_template("AdminViewDonations.html",data=data)


@admin.route('/AdminViewTeachingRequests')
def AdminViewTeachingRequests():
	data={}

	q="SELECT *,CONCAT(user.first_name,' ',user.last_name) AS uname FROM `teaching_requests` INNER JOIN `user` USING (`user_id`)"
	res=select(q)
	data['or']=res
	return render_template("AdminViewTeachingRequests.html",data=data)


# @admin.route('/AdminViewTestimonials')
# def AdminViewTestimonials():
# 	data={}

# 	q="SELECT * FROM feedback INNER JOIN `orphanage` USING (`orphanage_id`)"
# 	res=select(q)
# 	data['or']=res
# 	return render_template("AdminViewTestimonials.html",data=data)


