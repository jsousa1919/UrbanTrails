# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GoogleReference'
        db.create_table(u'trails_googlereference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'trails', ['GoogleReference'])

        # Adding model 'Venue'
        db.create_table(u'trails_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trails.GoogleReference'], null=True, blank=True)),
        ))
        db.send_create_signal(u'trails', ['Venue'])

        # Adding model 'Trail'
        db.create_table(u'trails_trail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'trails', ['Trail'])

        # Adding model 'TrailVenue'
        db.create_table(u'trails_trailvenue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trails.Trail'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trails.Venue'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'trails', ['TrailVenue'])


    def backwards(self, orm):
        # Deleting model 'GoogleReference'
        db.delete_table(u'trails_googlereference')

        # Deleting model 'Venue'
        db.delete_table(u'trails_venue')

        # Deleting model 'Trail'
        db.delete_table(u'trails_trail')

        # Deleting model 'TrailVenue'
        db.delete_table(u'trails_trailvenue')


    models = {
        u'trails.googlereference': {
            'Meta': {'object_name': 'GoogleReference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'trails.trail': {
            'Meta': {'object_name': 'Trail'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'trails.trailvenue': {
            'Meta': {'object_name': 'TrailVenue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'trail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trails.Trail']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trails.Venue']"})
        },
        u'trails.venue': {
            'Meta': {'object_name': 'Venue'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trails.GoogleReference']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trails']