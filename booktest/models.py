from django.db import models


# 自定义管理类
class BookInfoManager(models.Manager):
    def create_book(self, title, pub_date):
        # Todo 方式一需要save()
        # b = self.model()  # 调用类对象
        # b.btitle = title
        # b.bpub_date = pub_date
        # b.bread = 0
        # b.bcommet = 0
        # b.isDelete = False
        # return b
        # Todo 方式二不需要save()
        book = self.create(btitle=title, bpub_date=pub_date, bread=0, bcommet=0, isDelete=False)
        return book


# 书模块

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    class Meta():
        db_table = 'bookinfo'

    book1 = BookInfoManager()

    @classmethod
    def create(cls, title, pub_date):
        book = cls(btitle=title, bpub_date=pub_date)
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        return book


# 英雄模块
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE, )


    def __str__(self):
        return self.hname