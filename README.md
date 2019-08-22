# SherpaDerp
All-in-one software for DDL.

SherpaDerp is software that unites administrative processes for the Sales People, Administrators, Accounting, Service Dispatch, and Executives at DDL, in one software suite. 
The need for this software arose from the usage of multiple software packages that had a hard time communicating with one another.  We have one for accounting that doesn't include all the features we would like to have, another for sales people that looks like it was designed 15 years ago and has endless bugs, and another that spams your emails with useless information (which wouldn't be so bad except the notifications for everyone must be managed by one admin, so everything is just always on).  
An advantage of paying no licensing fees and having the software built in house to meet the exact needs of DDL was another driving factor. Because the software is specific to one company, it can be very lightweight and features can be added on the fly without paying inflated development costs to a third party.  The software can also be scaled to include more members of any part of the company without additional cost.  
Now instead of having to decide who 'really' needs a license and who doesn't, everyone has access.  When new employees join the company we don't have to commission new licenses, and if the company contracts, we aren't committed to too many licenses.
On top of all that, having a lightweight, streamlined, web-based software to use makes everything more efficient.  No more work arounds -- just fluid process.


Notes
-------------------------------------------------
USER STRUCTURE
- Directors (Perry, Jim, Lisa)
	- Reports	
	- simple mode / full priveleges mode.  In simple mode the directors will only see what they want to see -- Reports.  They will make their decisions and tell people what to do. No need for Administrative functions to clutter their UI.  But they should have the ability to click a button and enable "full priv mode" which would give them "accounting" abilities as well.  When they are done with it they can turn it off again and just see their favourite reports.
- Managers 
	- Reports
	- Sales funnel (still need more info on what this is)
	- Rep stats
	- Leasing and customer info
- Sales Reps
	- Customer Equipment
	- Lease tracker
	- Proposals (with config validation)
	- Paperwork
	- Submit Orders (as quotes to admin team)
	- Prospect management
	- Sales teams
	- Sales Zones
	- "named" accounts
	- Sales funnel (still need more info on what this is)
- Administrators (krishani, sumira, lisa, michelle)
	- orders (received as quotes, converted in to Sales Orders, then converted into invoices)
	- purchase orders
	- invoicing
	- receivables
	- on hold
	- accounting
	- customers
	- reports
- Accounting dept (lyra, Lisa)
	- everything administrators have +
	- Payables
	- Banking
	- Journal Entries
- Warehouse crew
	- dispatch centre tasks
	- inventory centre


ROLES
- roles should have access to modules (apps), and you assign users to groups which have roles assigned to them.


Dashboard
- the dashboard will be a widget section.  I'm currently envisioning a card layout with descriptions. You could maybe choose between the card layout and a simpler heiroglyphic style setup, where the name would show up on hover. like a circular logo with a hidden name underneath that shows when you hover the module.  Yah I like that.
- The roles would be easier to do because you would just have a list of widgets, or apps, and assign them to groups. You assign users to groups, and bam, they can see those widgets.
- This makes a flow where the user will come back to the dashboard to get a birds eye view of the things they can do, then select one and drill down into using it.
- Received receipts for documents could be cool.  Basically when you send an invoice or whatever from the system, in the email it asks the user to click a button showing they have received the invoice.  This way, if the user clicks that button, it will send a JSON response to the originator's account -- updating a little flag on the document to show "receipt confirmed".
- Administrators can "reject" orders and will be asked to give a reason.  This way, Lisa can just click "no, reject" and type a 2 second note like "missing BP#, and missing meter reads".
- Sales reps need a HUD where they can see in real-time whether or not their orders have been pushed back, completed, or are hanging in limbo.  It could function like a "last 5 actions" menu, where you could drill down into it to see the whole history of your orders.


MVP (Minimum Viable Product)
-------------------------------
-6 User types (with unique dashboards)
- Executives see a list of proposals, orders, quotes, invoices, POs created by everyone (grouped by team, etc?)
- Sales Reps can create proposals (start out with 1 static config)
- Sales Reps can create customers
- Sales Reps can see THEIR OWN proposals created (and status?)
- Administrators have order inbox
- Administrators can convert quotes to sales orders with 1 button.
- Administrators can convert sales orders to invoices.
- Administrators can convert POs to SOs.
- Administrators can see a list of SOs, POs, and invoices created by everyone.
- Administrators can create customers
- Accounting just exists for now as a copy of Admin
- Managers can just see lists of proposals created by reps on their team (and status?)
- Warehouse just exists for now, until I can fully understand their workflow and incorporate it.