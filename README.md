# HEALTHYHITO+


## Business Requirements
1. The Users can generate a meal
2. The Users can have a history of the meals they liked.
3. The Users will have a profile menu.
4. The Users will receive a notifications.
5. The Users can view the meal in details.

## API Definitions

### Authentication
Login
```sh
    /api/token/  
```

Signup
```sh
    /api/register/
```

### User Profile
Getting the user details 
```sh
    /api/user/details/{id}/
```

Updating the user details 
```sh
    /api/user/details/update/
```

### Meal Generation
Generating a meal
```sh
    /api/meal/
```

If user likes the meal, it will be save to database
```sh
    /api/meal/cook/
```

### Meal History
Getting all meal cooked/liked/accepted by the user
```sh
    /api/user/history/meals/
```

Getting the details of meal when viewing from meal history
```sh 
    /api/user/history/meal/{id}/
```

### Notifications
Getting all user notifications 
```sh
    /api/user/notifications/
```

Getting specific user notification
```sh
    /api/user/notifications/{id}/
```

Saving sent notification to user
 ```sh 
    /api/user/notifications/save-sent/
```

Marking all notifications as read
```sh
    /api/user/notifications/mark-all-read/
```

Read specific user notification
```sh
    /api/user/notifications/read/
```

Deleting all notifications
```sh
    /api/user/notifications/remove-all/
```

Delete specific user notification
```sh
    /api/user/notifications/remove/
```



