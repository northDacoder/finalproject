# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Developer'
        db.create_table(u'developer_app_developer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('languages', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'developer_app', ['Developer'])

        # Adding model 'Language'
        db.create_table(u'developer_app_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'developer_app', ['Language'])

        # Adding model 'Project'
        db.create_table(u'developer_app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['developer_app.Developer'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['developer_app.Language'])),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'developer_app', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Developer'
        db.delete_table(u'developer_app_developer')

        # Deleting model 'Language'
        db.delete_table(u'developer_app_language')

        # Deleting model 'Project'
        db.delete_table(u'developer_app_project')


    models = {
        u'developer_app.developer': {
            'Meta': {'object_name': 'Developer'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'developer_app.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'developer_app.project': {
            'Meta': {'object_name': 'Project'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['developer_app.Language']"}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['developer_app.Developer']"})
        }
    }

    complete_apps = ['developer_app']