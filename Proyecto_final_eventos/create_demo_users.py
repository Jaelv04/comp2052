from app import create_app, db
from app.models import Role, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
   
    print("🗑️ Dropping all tables...")
    db.drop_all()
    print("📦 Creating all tables...")
    db.create_all()
    
    print("\n👥 Creating roles...")
    roles = ['Admin', 'Organizador', 'Participante']  
    for role_name in roles:
        existing_role = Role.query.filter_by(name=role_name).first()
        if not existing_role:
            new_role = Role(name=role_name)
            db.session.add(new_role)
            print(f'✅ Role "{role_name}" created.')

    db.session.commit()

    # Updated user data with correct role names
    users_data = [
        {
            "username": "Administrator",
            "email": "admin@example.com",
            "password": "admin123",
            "role_name": "Admin"
        },
        {
            "username": "John Doe",
            "email": "org@example.com",
            "password": "org123",
            "role_name": "Organizador"  
        },
        {
            "username": "Steve Jobs",
            "email": "part@example.com",
            "password": "part123",
            "role_name": "Participante" 
        }
    ]

    for user_info in users_data:
        existing_user = User.query.filter_by(email=user_info['email']).first()
        if not existing_user:
            role = Role.query.filter_by(name=user_info['role_name']).first()
            if role:
                user = User(
                    username=user_info['username'],
                    email=user_info['email'],
                    role_id=role.id  
                )
                user.set_password(user_info['password'])
                db.session.add(user)
                print(f'✅ User "{user.username}" created with role "{role.name}"')
            else:
                print(f'❌ Role "{user_info["role_name"]}" not found!')
        else:
            print(f'ℹ️ User with email {user_info["email"]} already exists.')

    db.session.commit()
    print("\n✅ All users processed successfully!")
