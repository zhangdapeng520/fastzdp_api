import fastzdp_sqlmodel as fasm
from fastzdp_api import Api
import routers

engine = fasm.get_engine(password="zhangdapeng520", database="fastzdp_sqlmodel")
app = Api()
app.include_router(routers.get_classes_router(engine))

if __name__ == '__main__':
    app.run()
