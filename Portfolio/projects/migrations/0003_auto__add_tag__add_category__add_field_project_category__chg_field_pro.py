# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'projects_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'projects', ['Tag'])

        # Adding model 'Category'
        db.create_table(u'projects_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'projects', ['Category'])

        # Adding field 'Project.category'
        db.add_column(u'projects_project', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Category'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field tags on 'Project'
        db.create_table(u'projects_project_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('tag', models.ForeignKey(orm[u'projects.tag'], null=False))
        ))
        db.create_unique(u'projects_project_tags', ['project_id', 'tag_id'])


        # Changing field 'Project.description'
        db.alter_column(u'projects_project', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Project.created'
        db.alter_column(u'projects_project', 'created', self.gf('django.db.models.fields.DateTimeField')())
        # Adding field 'Post.category'
        db.add_column(u'projects_post', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Category'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field tags on 'Post'
        db.create_table(u'projects_post_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'projects.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'projects.tag'], null=False))
        ))
        db.create_unique(u'projects_post_tags', ['post_id', 'tag_id'])


        # Changing field 'Post.created'
        db.alter_column(u'projects_post', 'created', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'projects_tag')

        # Deleting model 'Category'
        db.delete_table(u'projects_category')

        # Deleting field 'Project.category'
        db.delete_column(u'projects_project', 'category_id')

        # Removing M2M table for field tags on 'Project'
        db.delete_table('projects_project_tags')


        # Changing field 'Project.description'
        db.alter_column(u'projects_project', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Project.created'
        db.alter_column(u'projects_project', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Post.category'
        db.delete_column(u'projects_post', 'category_id')

        # Removing M2M table for field tags on 'Post'
        db.delete_table('projects_post_tags')


        # Changing field 'Post.created'
        db.alter_column(u'projects_post', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'projects.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'projects.post': {
            'Meta': {'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {}),
            'github_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'live_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'summary': ('tinymce.models.HTMLField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        u'projects.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']