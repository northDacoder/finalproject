# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Company.city'
        db.alter_column(u'company_app_company', 'city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Company.github'
        db.alter_column(u'company_app_company', 'github', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True))

        # Changing field 'Company.description'
        db.alter_column(u'company_app_company', 'description', self.gf('django.db.models.fields.TextField')(max_length=6000, null=True))

        # Changing field 'Company.screenshot'
        db.alter_column(u'company_app_company', 'screenshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Company.cover'
        db.alter_column(u'company_app_company', 'cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Company.state'
        db.alter_column(u'company_app_company', 'state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Company.email'
        db.alter_column(u'company_app_company', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'CompanyProject.description'
        db.alter_column(u'company_app_companyproject', 'description', self.gf('django.db.models.fields.TextField')(max_length=6000, null=True))

        # Changing field 'CompanyProject.language'
        db.alter_column(u'company_app_companyproject', 'language_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company_app.Language'], null=True))

        # Changing field 'CompanyProject.project_screenshot'
        db.alter_column(u'company_app_companyproject', 'project_screenshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Company.city'
        raise RuntimeError("Cannot reverse this migration. 'Company.city' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.city'
        db.alter_column(u'company_app_company', 'city', self.gf('django.db.models.fields.CharField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'Company.github'
        raise RuntimeError("Cannot reverse this migration. 'Company.github' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.github'
        db.alter_column(u'company_app_company', 'github', self.gf('django.db.models.fields.URLField')(max_length=1000))

        # Changing field 'Company.description'
        db.alter_column(u'company_app_company', 'description', self.gf('django.db.models.fields.TextField')(default=1, max_length=6000))

        # Changing field 'Company.screenshot'
        db.alter_column(u'company_app_company', 'screenshot', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100))

        # Changing field 'Company.cover'
        db.alter_column(u'company_app_company', 'cover', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100))

        # Changing field 'Company.state'
        db.alter_column(u'company_app_company', 'state', self.gf('django.db.models.fields.CharField')(default=1, max_length=100))

        # Changing field 'Company.email'
        db.alter_column(u'company_app_company', 'email', self.gf('django.db.models.fields.EmailField')(default=1, max_length=75))

        # Changing field 'CompanyProject.description'
        db.alter_column(u'company_app_companyproject', 'description', self.gf('django.db.models.fields.TextField')(default=1, max_length=6000))

        # Changing field 'CompanyProject.language'
        db.alter_column(u'company_app_companyproject', 'language_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['company_app.Language']))

        # Changing field 'CompanyProject.project_screenshot'
        db.alter_column(u'company_app_companyproject', 'project_screenshot', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'company_app.company': {
            'Meta': {'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'company_app.companyproject': {
            'Meta': {'object_name': 'CompanyProject'},
            'accepted_project': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'company_pick'", 'unique': 'True', 'null': 'True', 'to': u"orm['developer_app.DeveloperProject']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company_app.Company']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company_app.Language']", 'null': 'True', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'project_screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'company_app.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'developer_app.developer': {
            'Meta': {'object_name': 'Developer'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '6000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['company_app.Language']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'developer_app.developerproject': {
            'Meta': {'object_name': 'DeveloperProject'},
            'company_project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'developer_projects'", 'to': u"orm['company_app.CompanyProject']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '6000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': u"orm['developer_app.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'project_screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['company_app']