# used class based view instead of method based
"""
@login_required
def Build_Kb(request):
    if request.method == 'POST':
        form = Build_kbform(request.user, request.POST)
        if form.is_valid():
            cuemail_id = request.user.email
            knowledge_category = form.cleaned_data.get("Knowledge_category")
            title = form.cleaned_data.get("title")
            knowledge = form.cleaned_data.get("knowledge")
            keywords = form.cleaned_data.get("keywords")
            share_with = form.cleaned_data.get("share_with")
            instance = Buildkb.objects.create(email=cuemail_id, knowledge_category=knowledge_category, title=title,
                                              knowledge=knowledge, keywords=keywords, share_with=share_with)
            for user in share_with:
                instance.share_with.add(user)
                instance.save()
            return redirect('/')
    else:
        form = Build_kbform(request.user)
    return render(request, 'pkm_templates/buildkb.html', {'form': form})
"""
"""
def set_user(request):
    if request.method == "POST":
        form = Set_User_Form(request.POST)
        if form.is_valid():
            org=form.cleaned_data.get('organization')
            email=form.cleaned_data.get('email_id')
            Desig=form.cleaned_data.get("Designation")
            job=form.cleaned_data.get("job_level")
            emails=form.cleaned_data.get("share_email_with")
            instance=Setup_user(organization=org,email_id=email,Designation=Desig,job_level=job,emails_for_help=emails)
            instance.save()
            return HttpResponse("form saved")

    else:
        form = Set_User_Form()

    return render(request, "pkm_templates/set_up_user.html", {'form': form})
"""


"""
unused packages
multifield
django-filters
"""

"""
{% load staticfiles %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tree Structure</title>
	<style>
		body {
			font-family: Arial;
			}
		ul.tree li {
			list-style-type: none;
			position: relative;
		}
		ul.tree li ul {
			display: none;
		}
		ul.tree li.open > ul {
			display: block;
		}
		ul.tree li a {
			color: black;
			text-decoration: none;
		}
		ul.tree li a:before {
			height: 1em;
			padding:0 .1em;
			font-size: .8em;
			display: block;
			position: absolute;
			left: -1.3em;
			top: .2em;
		}
		ul.tree li > a:not(:last-child):before {
			content: '+';
		}
		ul.tree li.open > a:not(:last-child):before {
			content: '-';
		}
	</style>
</head>
<body>
	<ul class="tree">
	  <li><a href="#">Part 1</a>
		<ul>
		  <li><a href="#">Item A</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item B</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item C</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>

		</ul>
	  </li>
	  <li><a href="#">Part 2</a>
		<ul>
		  <li><a href="#">Item A</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item B</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item C</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>

		</ul>
	  </li>
	  <li><a href="#">Part 3</a>
		<ul>
		  <li><a href="#">Item A</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item B</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		  <li><a href="#">Item C</a>
			<ul>
			  <li><a href="#">Sub-item 1</a></li>
			  <li><a href="#">Sub-item 2</a></li>
			  <li><a href="#">Sub-item 3</a></li>
			</ul>
		  </li>
		</ul>
	  </li>
	</ul>
	<script type="text/javascript" language="javascript">
		var tree = document.querySelectorAll('ul.tree a:not(:last-child)');
		for(var i = 0; i < tree.length; i++){
			tree[i].addEventListener('click', function(e) {
				var parent = e.target.parentElement;
				var classList = parent.classList;
				if(classList.contains("open")) {
					classList.remove('open');
					var opensubs = parent.querySelectorAll(':scope .open');
					for(var i = 0; i < opensubs.length; i++){
						opensubs[i].classList.remove('open');
					}
				} else {
					classList.add('open');
				}
			});
		}
	</script>
</body>
</html>
"""