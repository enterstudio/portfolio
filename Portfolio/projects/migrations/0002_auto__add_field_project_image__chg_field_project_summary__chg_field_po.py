# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.image'
        db.add_column(u'projects_project', 'image',
                      self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Project.summary'
        db.alter_column(u'projects_project', 'summary', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Post.content'
        db.alter_column(u'projects_post', 'content', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):
        # Deleting field 'Project.image'
        db.delete_column(u'projects_project', 'image')


        # Changing field 'Project.summary'
        db.alter_column(u'projects_project', 'summary', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Post.content'
        db.alter_column(u'projects_post', 'content', self.gf('django.db.models.fields.TextField')())

    models = {
        u'projects.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'github_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'live_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'summary': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['projects']