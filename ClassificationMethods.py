#Python OOP yapısı kullanılmıştır.
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics,preprocessing, model_selection
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns



class YontemML:
  def __init__(self, X,y) :
      self.X = X
      self.y=  y
      self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.33,random_state=42)

  def Logistic(self):
    print("*****Logistic Regression*****")
    loj_model=LogisticRegression().fit(self.X_train,self.y_train)
    y_pred_loj=loj_model.predict(self.X_test)
    loj_skor= accuracy_score(y_pred_loj,self.y_test)
    print('Model Dogrulugu:', loj_skor)
    print("Classification report")
    cf_matrix_loj=confusion_matrix(y_pred_loj,self.y_test)
    sns.heatmap(cf_matrix_loj,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(loj_skor))
    print(classification_report(y_pred_loj,self.y_test))


  def Knn(self):
    print("*****KNN Algoritmasi*****")
    knn_model=KNeighborsClassifier().fit(self.X_train,self.y_train)
    y_pred_knn=knn_model.predict(self.X_test)
    knn_skor= accuracy_score(y_pred_knn,self.y_test)
    print('Model Dogrulugu:', knn_skor)
    print("Classification report")
    cf_matrix_knn=confusion_matrix(y_pred_knn,self.y_test)
    sns.heatmap(cf_matrix_knn,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(knn_skor))
    print(classification_report(y_pred_knn,self.y_test))


  def Svm(self):
    print("*****SVM Algoritmasi*****")
    svm_model=SVC().fit(self.X_train,self.y_train)
    y_pred_svm=svm_model.predict(self.X_test)
    svm_skor= accuracy_score(y_pred_svm,self.y_test)
    print('Model Dogrulugu:', svm_skor)
    print("Classification report")
    cf_matrix_svm=confusion_matrix(y_pred_svm,self.y_test)
    sns.heatmap(cf_matrix_svm,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(svm_skor))
    print(classification_report(y_pred_svm,self.y_test))


  def Decisiontree(self):
    print("*****Decision Tree Algoritmasi*****")
    cart_model=DecisionTreeClassifier().fit(self.X_train,self.y_train)
    y_pred_cart=cart_model.predict(self.X_test)
    cart_skor= accuracy_score(y_pred_cart,self.y_test)
    print('Model Dogrulugu:', cart_skor)
    print("Classification report")
    cf_matrix_cart=confusion_matrix(y_pred_cart,self.y_test)
    sns.heatmap(cf_matrix_cart,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(cart_skor))
    print(classification_report(y_pred_cart,self.y_test))


  def Randomforest(self):
    print("*****Random Forest Algoritmasi*****")
    rf_model=RandomForestClassifier().fit(self.X_train,self.y_train)
    y_pred_rf=rf_model.predict(self.X_test)
    rf_skor= accuracy_score(y_pred_rf,self.y_test)
    print('Model Dogrulugu:', rf_skor)
    print("Classification report")
    cf_matrix_rf=confusion_matrix(y_pred_rf,self.y_test)
    sns.heatmap(cf_matrix_rf,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(rf_skor))
    print(classification_report(y_pred_rf,self.y_test))


  def Xgboost(self):
    print("*****XGBoost Algoritmasi*****")
    xgbm_model=XGBClassifier().fit(self.X_train,self.y_train)
    y_pred_xgbm=xgbm_model.predict(self.X_test)
    xgbm_skor= accuracy_score(y_pred_xgbm,self.y_test)
    print('Model Dogrulugu:', xgbm_skor)
    print("Classification report")
    cf_matrix_xgbm=confusion_matrix(y_pred_xgbm,self.y_test)
    sns.heatmap(cf_matrix_xgbm,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(xgbm_skor))
    print(classification_report(y_pred_xgbm,self.y_test))


  def Gbm(self):
    print("*****GBM Algoritmasi*****")
    gbm_model=GradientBoostingClassifier().fit(self.X_train,self.y_train)
    y_pred_gbm=gbm_model.predict(self.X_test)
    gbm_skor= accuracy_score(y_pred_gbm,self.y_test)
    print('Model Dogrulugu:', gbm_skor)
    print("Classification report")
    cf_matrix_gbm=confusion_matrix(y_pred_gbm,self.y_test)
    sns.heatmap(cf_matrix_gbm,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(gbm_skor))
    print(classification_report(y_pred_gbm,self.y_test))

  def LightGBM(self):
    print("*****Light GBM Algoritmasi*****")
    lgbm_model=LGBMClassifier().fit(self.X_train,self.y_train)
    y_pred_lgbm=lgbm_model.predict(self.X_test)
    lgbm_skor= accuracy_score(y_pred_lgbm,self.y_test)
    print('Model Dogrulugu:', lgbm_skor)
    print("Classification report")
    cf_matrix_lgbm=confusion_matrix(y_pred_lgbm,self.y_test)
    sns.heatmap(cf_matrix_lgbm,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(lgbm_skor))
    print(classification_report(y_pred_lgbm,self.y_test))


  def Mlpc(self):
    print("*****MLPC Algoritmasi*****")
    mlpc_model=MLPClassifier().fit(self.X_train,self.y_train)
    y_pred_mlpc=mlpc_model.predict(self.X_test)
    mlpc_skor= accuracy_score(y_pred_mlpc,self.y_test)
    print('Model Dogrulugu:', mlpc_skor)
    print("Classification report")
    cf_matrix_mlpc=confusion_matrix(y_pred_mlpc,self.y_test)
    sns.heatmap(cf_matrix_mlpc,annot=True,cbar=False, fmt='g')
    plt.title("Model Doğruluğu:"+str(mlpc_skor))
    print(classification_report(y_pred_mlpc,self.y_test))
