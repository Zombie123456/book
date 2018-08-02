from __future__ import unicode_literals
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.



class S1(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '《漂亮女医生的风雨爱情》'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '《漂亮女医生的风雨爱情》'
    def url(self):
        return '/index/story/?name=S1'

class S2(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '万能高手'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '万能高手'
    def url(self):
        return '/index/story/?name=S2'

class S3(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '上古神王'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '上古神王'
    def url(self):
        return '/index/story/?name=S3'

class S4(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '不朽音魔'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '不朽音魔'
    def url(self):
        return '/index/story/?name=S4'

class S5(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '九界无仙'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '九界无仙'
    def url(self):
        return '/index/story/?name=S5'

class S6(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '任性老婆好V5'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '任性老婆好V5'
    def url(self):
        return '/index/story/?name=S6'

class S7(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '傲世圣灵'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '傲世圣灵'
    def url(self):
        return '/index/story/?name=S7'

class S8(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '兽血沸腾'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '兽血沸腾'
    def url(self):
        return '/index/story/?name=S8'

class S9(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '凤求凰'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '凤求凰'
    def url(self):
        return '/index/story/?name=S9'

class S10(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '医科圣手'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '医科圣手'
    def url(self):
        return '/index/story/?name=S10'

class S11(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '召唤狂人在异界'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '召唤狂人在异界'
    def url(self):
        return '/index/story/?name=S11'

class S12(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '天门鬼道'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '天门鬼道'
    def url(self):
        return '/index/story/?name=S12'

class S13(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '女仆的异界传说'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '女仆的异界传说'
    def url(self):
        return '/index/story/?name=S13'

class S14(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '少将的纯情宝贝'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '少将的纯情宝贝'
    def url(self):
        return '/index/story/?name=S4'

class S15(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '巾帼娇'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '巾帼娇'
    def url(self):
        return '/index/story/?name=S15'

class S16(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '御道'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '御道'
    def url(self):
        return '/index/story/?name=S16'

class S17(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '战帝'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '战帝'
    def url(self):
        return '/index/story/?name=S17'

class S18(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '护花狂尸'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '护花狂尸'
    def url(self):
        return '/index/story/?name=S18'

class S19(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '拳灭天穹'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '拳灭天穹'
    def url(self):
        return '/index/story/?name=S19'

class S20(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '无限进化'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '无限进化'
    def url(self):
        return '/index/story/?name=S20'

class S21(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '权路'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '权路'
    def url(self):
        return '/index/story/?name=S21'

class S22(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '极品司机'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '极品司机'
    def url(self):
        return '/index/story/?name=S22'

class S23(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '极度尸寒'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '极度尸寒'
    def url(self):
        return '/index/story/?name=S23'

class S24(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '校园妙手神医'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '校园妙手神医'
    def url(self):
        return '/index/story/?name=S24'

class S25(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '校花的极品高手'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '校花的极品高手'
    def url(self):
        return '/index/story/?name=S25'

class S26(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '校花的近身高手'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '校花的近身高手'
    def url(self):
        return '/index/story/?name=S26'

class S27(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '武侠重生'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '武侠重生'
    def url(self):
        return '/index/story/?name=S27'

class S28(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '武极乾坤'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '武极乾坤'
    def url(self):
        return '/index/story/?name=S28'

class S29(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '猎巫之王'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '猎巫之王'
    def url(self):
        return '/index/story/?name=S29'

class S30(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '电影中的兑换强者'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '电影中的兑换强者'
    def url(self):
        return '/index/story/?name=S30'

class S31(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '秋叶原之魔鬼经纪人'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '秋叶原之魔鬼经纪人'
    def url(self):
        return '/index/story/?name=S31'

class S32(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '纯情花嫁'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '纯情花嫁'
    def url(self):
        return '/index/story/?name=S32'

class S33(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '职场小白升职记'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '职场小白升职记'
    def url(self):
        return '/index/story/?name=S33'

class S34(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '背后高手'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '背后高手'
    def url(self):
        return '/index/story/?name=S34'

class S35(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '越狱红莲：邻家小妹是恶魔'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '越狱红莲：邻家小妹是恶魔'
    def url(self):
        return '/index/story/?name=S35'

class S36(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '足球豪门'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '足球豪门'
    def url(self):
        return '/index/story/?name=S36'

class S37(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '都市女秘书'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '都市女秘书'
    def url(self):
        return '/index/story/?name=S37'

class S38(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '重生之名门千金'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '重生之名门千金'
    def url(self):
        return '/index/story/?name=S38'

class S39(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '重生之嫡非良善'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '重生之嫡非良善'
    def url(self):
        return '/index/story/?name=S39'

class S40(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '野蛮女友'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '野蛮女友'
    def url(self):
        return '/index/story/?name=S40'

class S41(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '阴阳手眼'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '阴阳手眼'
    def url(self):
        return '/index/story/?name=S41'

class S42(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '隐宠爱妻'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '隐宠爱妻'
    def url(self):
        return '/index/story/?name=S42'

class S43(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '霉妃瑟舞'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '霉妃瑟舞'
    def url(self):
        return '/index/story/?name=S43'

class S44(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '霸情冷少，勿靠近'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '霸情冷少，勿靠近'
    def url(self):
        return '/index/story/?name=S44'

class S45(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '霸情恶少：调教小逃妻'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '霸情恶少：调教小逃妻'
    def url(self):
        return '/index/story/?name=S45'

class S46(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '霸气宝宝：带着娘亲闯江湖'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '霸气宝宝：带着娘亲闯江湖'
    def url(self):
        return '/index/story/?name=S46'

class S47(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '霸道首席毒宠美妻'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '霸道首席毒宠美妻'
    def url(self):
        return '/index/story/?name=S47'

class S48(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '青春的死胡同'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '青春的死胡同'
    def url(self):
        return '/index/story/?name=S48'

class S49(models.Model):
    chapter = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '魔手系统'
    def __str__(self):
        return self.chapter
    def table_name(self):
        return '魔手系统'
    def url(self):
        return '/index/story/?name=S49'



