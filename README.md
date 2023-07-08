## **Laravel tourism management system** 

**Utalii** is built on Laravel 8

There are 3 types of user accounts. They include:
 
- Administrators (Super Admin & Admin)
- Guest

**Requirements** 

Check Laravel 8 Requirements https://laravel.com/docs/8.x

**Installation**
- Install dependencies (composer install)
- Set Database Credentials & App Settings in dotenv file (.env)
- Migrate Database (php artisan migrate)
- Database seed (php artisan db:seed)

**Login Credentials**
After seeding. Login details as follows:

| Account Type  | Username | Email | Password |
| ------------- | -------- | ----- | -------- |
| Super Admin | cj | cj@cj.com | cj |
|  Admin | admin | admin@admin.com | cj |
|  guest | guest | guest@guest.com | cj |

#### **FUNCTIONS OF ACCOUNTS** 

**-- SUPER ADMIN**
- Only Super Admin can delete any record
- Create any user account
 
**-- Administrators (Super Admin & Admin)**

- Manage Users (Create, Edit and manage all user accounts & profiles)
- Manage Places (Create, Edit and manage all places or touristic sites)
- Manage Budgeting form
- Manage reports
- Edit system settings


**-- guest**
- Manage Own account
- Use budgeting form
- View touristic sites available
- Favourite touristic sites

**Utilizing the budgeting feature by ML**
-Clone "Samwel17\Utalii-FlaskAPI" repository
-Install the flask app requirements
- Run the flask application
- Run the Laravel application ( on different CMD simultaneously)


