from app.models.ums_admin import UmsAdmin as AdminModel


class UmsAdmin:

    def __init__(self):
        self.ums_admin_list = []
        self.ums_admin_list.append(AdminModel(1, 'admin', '123456', 'admin@example.com', 'admin', 1))
        self.ums_admin_list.append(AdminModel(2, 'test', '123456', 'test@example.com', 'test', 0))
        self.ums_admin_list.append(AdminModel(3, 'test2', '123456', 'test2@example.com', 'test2', 0))
        self.ums_admin_list.append(AdminModel(4, 'test3', '123456', 'test3@example.com', 'test3', 0))


    def get_admin(self, username: str, password: str):
        for admin in self.ums_admin_list:
            if admin.username == username and admin.password == password:
                return admin
        return None

    def insert(self, admin: AdminModel):
        self.ums_admin_list.append(admin)
        return 0

    def get_admin_by_username(self, username: str):
        for admin in self.ums_admin_list:
            if admin.username == username:
                return admin
        return  None