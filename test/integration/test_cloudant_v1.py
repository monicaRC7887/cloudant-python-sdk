# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for CloudantV1
"""

import os
import pytest
from ibmcloudant.cloudant_v1 import *

# Config file name
config_file = 'cloudant_v1.env'

class TestCloudantV1():
    """
    Integration Test Class for CloudantV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.cloudant_service = CloudantV1.new_instance(
                )
            assert cls.cloudant_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_server_information(self):

        get_server_information_response = self.cloudant_service.get_server_information()

        assert get_server_information_response.get_status_code() == 200
        server_information = get_server_information_response.get_result()
        assert server_information is not None

    @needscredentials
    def test_get_membership_information(self):

        get_membership_information_response = self.cloudant_service.get_membership_information()

        assert get_membership_information_response.get_status_code() == 200
        membership_information = get_membership_information_response.get_result()
        assert membership_information is not None

    @needscredentials
    def test_get_uuids(self):

        get_uuids_response = self.cloudant_service.get_uuids(
            count=1
        )

        assert get_uuids_response.get_status_code() == 200
        uuids_result = get_uuids_response.get_result()
        assert uuids_result is not None

    @needscredentials
    def test_head_database(self):

        head_database_response = self.cloudant_service.head_database(
            db='testString'
        )

        assert head_database_response.get_status_code() == 200

    @needscredentials
    def test_get_all_dbs(self):

        get_all_dbs_response = self.cloudant_service.get_all_dbs(
            descending=True,
            endkey='testString',
            limit=0,
            skip=0,
            startkey='testString'
        )

        assert get_all_dbs_response.get_status_code() == 200
        result = get_all_dbs_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_dbs_info(self):

        post_dbs_info_response = self.cloudant_service.post_dbs_info(
            keys=['testString']
        )

        assert post_dbs_info_response.get_status_code() == 200
        list_dbs_info_result = post_dbs_info_response.get_result()
        assert list_dbs_info_result is not None

    @needscredentials
    def test_get_database_information(self):

        get_database_information_response = self.cloudant_service.get_database_information(
            db='testString'
        )

        assert get_database_information_response.get_status_code() == 200
        database_information = get_database_information_response.get_result()
        assert database_information is not None

    @needscredentials
    def test_put_database(self):

        put_database_response = self.cloudant_service.put_database(
            db='testString',
            partitioned=True,
            q=1
        )

        assert put_database_response.get_status_code() == 201
        ok = put_database_response.get_result()
        assert ok is not None

    @needscredentials
    def test_post_changes(self):

        post_changes_response = self.cloudant_service.post_changes(
            db='testString',
            doc_ids=['testString'],
            fields=['testString'],
            selector={},
            last_event_id='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            feed='continuous',
            filter='testString',
            heartbeat=0,
            include_docs=True,
            limit=0,
            seq_interval=1,
            since='testString',
            style='testString',
            timeout=0,
            view='testString'
        )

        assert post_changes_response.get_status_code() == 200
        changes_result = post_changes_response.get_result()
        assert changes_result is not None

    @needscredentials
    def test_post_changes_as_stream(self):

        post_changes_as_stream_response = self.cloudant_service.post_changes_as_stream(
            db='testString',
            doc_ids=['testString'],
            fields=['testString'],
            selector={},
            last_event_id='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            feed='continuous',
            filter='testString',
            heartbeat=0,
            include_docs=True,
            limit=0,
            seq_interval=1,
            since='testString',
            style='testString',
            timeout=0,
            view='testString'
        )

        assert post_changes_as_stream_response.get_status_code() == 200
        result = post_changes_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_head_document(self):

        head_document_response = self.cloudant_service.head_document(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            latest=True,
            rev='testString'
        )

        assert head_document_response.get_status_code() == 200

    @needscredentials
    def test_post_document(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'foo': { 'foo': 'bar' }
        }

        post_document_response = self.cloudant_service.post_document(
            db='testString',
            document=document_model,
            content_type='application/json',
            batch='ok'
        )

        assert post_document_response.get_status_code() == 201
        document_result = post_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_post_all_docs(self):

        post_all_docs_response = self.cloudant_service.post_all_docs(
            db='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString'
        )

        assert post_all_docs_response.get_status_code() == 200
        all_docs_result = post_all_docs_response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_all_docs_as_stream(self):

        post_all_docs_as_stream_response = self.cloudant_service.post_all_docs_as_stream(
            db='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString'
        )

        assert post_all_docs_as_stream_response.get_status_code() == 200
        result = post_all_docs_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_all_docs_queries(self):

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': 'testString',
            'key': 'testString',
            'keys': ['testString'],
            'startkey': 'testString'
        }

        post_all_docs_queries_response = self.cloudant_service.post_all_docs_queries(
            db='testString',
            queries=[all_docs_query_model]
        )

        assert post_all_docs_queries_response.get_status_code() == 200
        all_docs_queries_result = post_all_docs_queries_response.get_result()
        assert all_docs_queries_result is not None

    @needscredentials
    def test_post_all_docs_queries_as_stream(self):

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': 'testString',
            'key': 'testString',
            'keys': ['testString'],
            'startkey': 'testString'
        }

        post_all_docs_queries_as_stream_response = self.cloudant_service.post_all_docs_queries_as_stream(
            db='testString',
            queries=[all_docs_query_model]
        )

        assert post_all_docs_queries_as_stream_response.get_status_code() == 200
        result = post_all_docs_queries_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_docs(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'foo': { 'foo': 'bar' }
        }

        # Construct a dict representation of a BulkDocs model
        bulk_docs_model = {
            'docs': [document_model],
            'new_edits': True
        }

        post_bulk_docs_response = self.cloudant_service.post_bulk_docs(
            db='testString',
            bulk_docs=bulk_docs_model
        )

        assert post_bulk_docs_response.get_status_code() == 201
        list_document_result = post_bulk_docs_response.get_result()
        assert list_document_result is not None

    @needscredentials
    def test_post_bulk_get(self):

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['testString'],
            'id': 'testString',
            'open_revs': ['testString'],
            'rev': 'testString'
        }

        post_bulk_get_response = self.cloudant_service.post_bulk_get(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=True,
            att_encoding_info=True,
            latest=True,
            revs=True
        )

        assert post_bulk_get_response.get_status_code() == 200
        bulk_get_result = post_bulk_get_response.get_result()
        assert bulk_get_result is not None

    @needscredentials
    def test_post_bulk_get_as_mixed(self):

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['testString'],
            'id': 'foo',
            'open_revs': ['testString'],
            'rev': '4-753875d51501a6b1883a9d62b4d33f91'
        }

        post_bulk_get_as_mixed_response = self.cloudant_service.post_bulk_get_as_mixed(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=True,
            att_encoding_info=True,
            latest=True,
            revs=True
        )

        assert post_bulk_get_as_mixed_response.get_status_code() == 200
        result = post_bulk_get_as_mixed_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_get_as_related(self):

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['testString'],
            'id': 'foo',
            'open_revs': ['testString'],
            'rev': '4-753875d51501a6b1883a9d62b4d33f91'
        }

        post_bulk_get_as_related_response = self.cloudant_service.post_bulk_get_as_related(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=True,
            att_encoding_info=True,
            latest=True,
            revs=True
        )

        assert post_bulk_get_as_related_response.get_status_code() == 200
        result = post_bulk_get_as_related_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_get_as_stream(self):

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['testString'],
            'id': 'foo',
            'open_revs': ['testString'],
            'rev': '4-753875d51501a6b1883a9d62b4d33f91'
        }

        post_bulk_get_as_stream_response = self.cloudant_service.post_bulk_get_as_stream(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=True,
            att_encoding_info=True,
            latest=True,
            revs=True
        )

        assert post_bulk_get_as_stream_response.get_status_code() == 200
        result = post_bulk_get_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document(self):

        get_document_response = self.cloudant_service.get_document(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_document_response.get_status_code() == 200
        document = get_document_response.get_result()
        assert document is not None

    @needscredentials
    def test_get_document_as_mixed(self):

        get_document_as_mixed_response = self.cloudant_service.get_document_as_mixed(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_document_as_mixed_response.get_status_code() == 200
        result = get_document_as_mixed_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document_as_related(self):

        get_document_as_related_response = self.cloudant_service.get_document_as_related(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_document_as_related_response.get_status_code() == 200
        result = get_document_as_related_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document_as_stream(self):

        get_document_as_stream_response = self.cloudant_service.get_document_as_stream(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_document_as_stream_response.get_status_code() == 200
        result = get_document_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_put_document(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'foo': { 'foo': 'bar' }
        }

        put_document_response = self.cloudant_service.put_document(
            db='testString',
            doc_id='testString',
            document=document_model,
            content_type='application/json',
            if_match='testString',
            batch='ok',
            new_edits=True,
            rev='testString'
        )

        assert put_document_response.get_status_code() == 201
        document_result = put_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_head_design_document(self):

        head_design_document_response = self.cloudant_service.head_design_document(
            db='testString',
            ddoc='testString',
            if_none_match='testString'
        )

        assert head_design_document_response.get_status_code() == 200

    @needscredentials
    def test_get_design_document(self):

        get_design_document_response = self.cloudant_service.get_design_document(
            db='testString',
            ddoc='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_design_document_response.get_status_code() == 200
        design_document = get_design_document_response.get_result()
        assert design_document is not None

    @needscredentials
    def test_put_design_document(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a Analyzer model
        analyzer_model = {
            'name': 'classic',
            'stopwords': ['testString']
        }

        # Construct a dict representation of a AnalyzerConfiguration model
        analyzer_configuration_model = {
            'name': 'classic',
            'stopwords': ['testString'],
            'fields': {}
        }

        # Construct a dict representation of a SearchIndexDefinition model
        search_index_definition_model = {
            'analyzer': analyzer_configuration_model,
            'index': 'testString'
        }

        # Construct a dict representation of a DesignDocumentOptions model
        design_document_options_model = {
            'partitioned': True
        }

        # Construct a dict representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model = {
            'map': 'testString',
            'reduce': 'testString'
        }

        # Construct a dict representation of a GeoIndexDefinition model
        geo_index_definition_model = {
            'index': 'testString'
        }

        # Construct a dict representation of a DesignDocument model
        design_document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'autoupdate': True,
            'filters': {},
            'indexes': {},
            'language': 'testString',
            'options': design_document_options_model,
            'updates': {},
            'validate_doc_update': {},
            'views': {},
            'st_indexes': {},
            'foo': { 'foo': 'bar' }
        }

        put_design_document_response = self.cloudant_service.put_design_document(
            db='testString',
            ddoc='testString',
            design_document=design_document_model,
            if_match='testString',
            batch='ok',
            new_edits=True,
            rev='testString'
        )

        assert put_design_document_response.get_status_code() == 201
        document_result = put_design_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_get_design_document_information(self):

        get_design_document_information_response = self.cloudant_service.get_design_document_information(
            db='testString',
            ddoc='testString'
        )

        assert get_design_document_information_response.get_status_code() == 200
        design_document_information = get_design_document_information_response.get_result()
        assert design_document_information is not None

    @needscredentials
    def test_post_design_docs(self):

        post_design_docs_response = self.cloudant_service.post_design_docs(
            db='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString',
            accept='application/json'
        )

        assert post_design_docs_response.get_status_code() == 200
        all_docs_result = post_design_docs_response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_design_docs_queries(self):

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': 'testString',
            'key': 'testString',
            'keys': ['testString'],
            'startkey': 'testString'
        }

        post_design_docs_queries_response = self.cloudant_service.post_design_docs_queries(
            db='testString',
            queries=[all_docs_query_model],
            accept='application/json'
        )

        assert post_design_docs_queries_response.get_status_code() == 200
        all_docs_queries_result = post_design_docs_queries_response.get_result()
        assert all_docs_queries_result is not None

    @needscredentials
    def test_post_view(self):

        post_view_response = self.cloudant_service.post_view(
            db='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey={ 'foo': 'bar' },
            endkey_docid='testString',
            group=True,
            group_level=1,
            key={ 'foo': 'bar' },
            keys=[{ 'foo': 'bar' }],
            reduce=True,
            stable=True,
            startkey={ 'foo': 'bar' },
            startkey_docid='testString',
            update='true'
        )

        assert post_view_response.get_status_code() == 200
        view_result = post_view_response.get_result()
        assert view_result is not None

    @needscredentials
    def test_post_view_as_stream(self):

        post_view_as_stream_response = self.cloudant_service.post_view_as_stream(
            db='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey={ 'foo': 'bar' },
            endkey_docid='testString',
            group=True,
            group_level=1,
            key={ 'foo': 'bar' },
            keys=[{ 'foo': 'bar' }],
            reduce=True,
            stable=True,
            startkey={ 'foo': 'bar' },
            startkey_docid='testString',
            update='true'
        )

        assert post_view_as_stream_response.get_status_code() == 200
        result = post_view_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_view_queries(self):

        # Construct a dict representation of a ViewQuery model
        view_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': { 'foo': 'bar' },
            'endkey_docid': 'testString',
            'group': True,
            'group_level': 1,
            'key': { 'foo': 'bar' },
            'keys': [{ 'foo': 'bar' }],
            'reduce': True,
            'stable': True,
            'startkey': { 'foo': 'bar' },
            'startkey_docid': 'testString',
            'update': 'true'
        }

        post_view_queries_response = self.cloudant_service.post_view_queries(
            db='testString',
            ddoc='testString',
            view='testString',
            queries=[view_query_model]
        )

        assert post_view_queries_response.get_status_code() == 200
        view_queries_result = post_view_queries_response.get_result()
        assert view_queries_result is not None

    @needscredentials
    def test_post_view_queries_as_stream(self):

        # Construct a dict representation of a ViewQuery model
        view_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': { 'foo': 'bar' },
            'endkey_docid': 'testString',
            'group': True,
            'group_level': 1,
            'key': { 'foo': 'bar' },
            'keys': [{ 'foo': 'bar' }],
            'reduce': True,
            'stable': True,
            'startkey': { 'foo': 'bar' },
            'startkey_docid': 'testString',
            'update': 'true'
        }

        post_view_queries_as_stream_response = self.cloudant_service.post_view_queries_as_stream(
            db='testString',
            ddoc='testString',
            view='testString',
            queries=[view_query_model]
        )

        assert post_view_queries_as_stream_response.get_status_code() == 200
        result = post_view_queries_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_partition_information(self):

        get_partition_information_response = self.cloudant_service.get_partition_information(
            db='testString',
            partition_key='testString'
        )

        assert get_partition_information_response.get_status_code() == 200
        partition_information = get_partition_information_response.get_result()
        assert partition_information is not None

    @needscredentials
    def test_post_partition_all_docs(self):

        post_partition_all_docs_response = self.cloudant_service.post_partition_all_docs(
            db='testString',
            partition_key='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString'
        )

        assert post_partition_all_docs_response.get_status_code() == 200
        all_docs_result = post_partition_all_docs_response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_partition_all_docs_as_stream(self):

        post_partition_all_docs_as_stream_response = self.cloudant_service.post_partition_all_docs_as_stream(
            db='testString',
            partition_key='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString'
        )

        assert post_partition_all_docs_as_stream_response.get_status_code() == 200
        result = post_partition_all_docs_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_search(self):

        post_partition_search_response = self.cloudant_service.post_partition_search(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            index='testString',
            query='testString',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='testString',
            highlight_pre_tag='testString',
            highlight_size=1,
            include_docs=True,
            include_fields=['testString'],
            limit=0,
            sort=['testString'],
            stale='ok'
        )

        assert post_partition_search_response.get_status_code() == 200
        search_result = post_partition_search_response.get_result()
        assert search_result is not None

    @needscredentials
    def test_post_partition_search_as_stream(self):

        post_partition_search_as_stream_response = self.cloudant_service.post_partition_search_as_stream(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            index='testString',
            query='testString',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='testString',
            highlight_pre_tag='testString',
            highlight_size=1,
            include_docs=True,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok'
        )

        assert post_partition_search_as_stream_response.get_status_code() == 200
        result = post_partition_search_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_view(self):

        post_partition_view_response = self.cloudant_service.post_partition_view(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey={ 'foo': 'bar' },
            endkey_docid='testString',
            group=True,
            group_level=1,
            key={ 'foo': 'bar' },
            keys=[{ 'foo': 'bar' }],
            reduce=True,
            stable=True,
            startkey={ 'foo': 'bar' },
            startkey_docid='testString',
            update='true'
        )

        assert post_partition_view_response.get_status_code() == 200
        view_result = post_partition_view_response.get_result()
        assert view_result is not None

    @needscredentials
    def test_post_partition_view_as_stream(self):

        post_partition_view_as_stream_response = self.cloudant_service.post_partition_view_as_stream(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey={ 'foo': 'bar' },
            endkey_docid='testString',
            group=True,
            group_level=1,
            key={ 'foo': 'bar' },
            keys=[{ 'foo': 'bar' }],
            reduce=True,
            stable=True,
            startkey={ 'foo': 'bar' },
            startkey_docid='testString',
            update='true'
        )

        assert post_partition_view_as_stream_response.get_status_code() == 200
        result = post_partition_view_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_find(self):

        post_partition_find_response = self.cloudant_service.post_partition_find(
            db='testString',
            partition_key='testString',
            selector={},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['testString'],
            limit=0,
            skip=0,
            sort=[{}],
            stable=True,
            update='false',
            use_index=['testString']
        )

        assert post_partition_find_response.get_status_code() == 200
        find_result = post_partition_find_response.get_result()
        assert find_result is not None

    @needscredentials
    def test_post_partition_find_as_stream(self):

        post_partition_find_as_stream_response = self.cloudant_service.post_partition_find_as_stream(
            db='testString',
            partition_key='testString',
            selector={},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['testString'],
            limit=0,
            skip=0,
            sort=[{}],
            stable=True,
            update='false',
            use_index=['testString']
        )

        assert post_partition_find_as_stream_response.get_status_code() == 200
        result = post_partition_find_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_explain(self):

        post_explain_response = self.cloudant_service.post_explain(
            db='testString',
            selector={},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['testString'],
            limit=0,
            skip=0,
            sort=[{}],
            stable=True,
            update='false',
            use_index=['testString'],
            r=1
        )

        assert post_explain_response.get_status_code() == 200
        explain_result = post_explain_response.get_result()
        assert explain_result is not None

    @needscredentials
    def test_post_find(self):

        post_find_response = self.cloudant_service.post_find(
            db='testString',
            selector={},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['testString'],
            limit=0,
            skip=0,
            sort=[{}],
            stable=True,
            update='false',
            use_index=['testString'],
            r=1
        )

        assert post_find_response.get_status_code() == 200
        find_result = post_find_response.get_result()
        assert find_result is not None

    @needscredentials
    def test_post_find_as_stream(self):

        post_find_as_stream_response = self.cloudant_service.post_find_as_stream(
            db='testString',
            selector={},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['testString'],
            limit=0,
            skip=0,
            sort=[{}],
            stable=True,
            update='false',
            use_index=['testString'],
            r=1
        )

        assert post_find_as_stream_response.get_status_code() == 200
        result = post_find_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_indexes_information(self):

        get_indexes_information_response = self.cloudant_service.get_indexes_information(
            db='testString'
        )

        assert get_indexes_information_response.get_status_code() == 200
        indexes_information = get_indexes_information_response.get_result()
        assert indexes_information is not None

    @needscredentials
    def test_post_index(self):

        # Construct a dict representation of a Analyzer model
        analyzer_model = {
            'name': 'classic',
            'stopwords': ['testString']
        }

        # Construct a dict representation of a IndexTextOperatorDefaultField model
        index_text_operator_default_field_model = {
            'analyzer': analyzer_model,
            'enabled': True
        }

        # Construct a dict representation of a IndexField model
        index_field_model = {
            'name': 'testString',
            'type': 'boolean',
            'foo': 'asc'
        }

        # Construct a dict representation of a IndexDefinition model
        index_definition_model = {
            'default_analyzer': analyzer_model,
            'default_field': index_text_operator_default_field_model,
            'fields': [index_field_model],
            'index_array_lengths': True
        }

        post_index_response = self.cloudant_service.post_index(
            db='testString',
            index=index_definition_model,
            ddoc='testString',
            def_=index_definition_model,
            name='testString',
            partial_filter_selector={},
            partitioned=True,
            type='json'
        )

        assert post_index_response.get_status_code() == 200
        index_result = post_index_response.get_result()
        assert index_result is not None

    @needscredentials
    def test_post_search_analyze(self):

        post_search_analyze_response = self.cloudant_service.post_search_analyze(
            analyzer='arabic',
            text='testString'
        )

        assert post_search_analyze_response.get_status_code() == 200
        search_analyze_result = post_search_analyze_response.get_result()
        assert search_analyze_result is not None

    @needscredentials
    def test_post_search(self):

        post_search_response = self.cloudant_service.post_search(
            db='testString',
            ddoc='testString',
            index='testString',
            query='testString',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='testString',
            highlight_pre_tag='testString',
            highlight_size=1,
            include_docs=True,
            include_fields=['testString'],
            limit=0,
            sort=['testString'],
            stale='ok',
            counts=['testString'],
            drilldown=[['testString']],
            group_field='testString',
            group_limit=1,
            group_sort=['testString'],
            ranges={}
        )

        assert post_search_response.get_status_code() == 200
        search_result = post_search_response.get_result()
        assert search_result is not None

    @needscredentials
    def test_post_search_as_stream(self):

        post_search_as_stream_response = self.cloudant_service.post_search_as_stream(
            db='testString',
            ddoc='testString',
            index='testString',
            query='testString',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='testString',
            highlight_pre_tag='testString',
            highlight_size=1,
            include_docs=True,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok',
            counts=['testString'],
            drilldown=[['testString']],
            group_field='testString',
            group_limit=1,
            group_sort=['testString'],
            ranges={}
        )

        assert post_search_as_stream_response.get_status_code() == 200
        result = post_search_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_search_info(self):

        get_search_info_response = self.cloudant_service.get_search_info(
            db='testString',
            ddoc='testString',
            index='testString'
        )

        assert get_search_info_response.get_status_code() == 200
        search_info_result = get_search_info_response.get_result()
        assert search_info_result is not None

    @needscredentials
    def test_get_geo(self):

        get_geo_response = self.cloudant_service.get_geo(
            db='testString',
            ddoc='testString',
            index='testString',
            bbox='testString',
            bookmark='testString',
            format='legacy',
            g='testString',
            include_docs=True,
            lat=-90,
            limit=0,
            lon=-180,
            nearest=True,
            radius=0,
            rangex=0,
            rangey=0,
            relation='contains',
            skip=0,
            stale='ok'
        )

        assert get_geo_response.get_status_code() == 200
        geo_result = get_geo_response.get_result()
        assert geo_result is not None

    @needscredentials
    def test_get_geo_as_stream(self):

        get_geo_as_stream_response = self.cloudant_service.get_geo_as_stream(
            db='testString',
            ddoc='testString',
            index='testString',
            bbox='testString',
            bookmark='testString',
            format='legacy',
            g='testString',
            include_docs=True,
            lat=-90,
            limit=0,
            lon=-180,
            nearest=True,
            radius=0,
            rangex=0,
            rangey=0,
            relation='contains',
            skip=0,
            stale='ok'
        )

        assert get_geo_as_stream_response.get_status_code() == 200
        result = get_geo_as_stream_response.get_result()
        assert result is not None

    @needscredentials
    def test_post_geo_cleanup(self):

        post_geo_cleanup_response = self.cloudant_service.post_geo_cleanup(
            db='testString'
        )

        assert post_geo_cleanup_response.get_status_code() == 202
        ok = post_geo_cleanup_response.get_result()
        assert ok is not None

    @needscredentials
    def test_get_geo_index_information(self):

        get_geo_index_information_response = self.cloudant_service.get_geo_index_information(
            db='testString',
            ddoc='testString',
            index='testString'
        )

        assert get_geo_index_information_response.get_status_code() == 200
        geo_index_information = get_geo_index_information_response.get_result()
        assert geo_index_information is not None

    @needscredentials
    def test_get_db_updates(self):

        get_db_updates_response = self.cloudant_service.get_db_updates(
            feed='continuous',
            heartbeat=0,
            timeout=0,
            since='testString'
        )

        assert get_db_updates_response.get_status_code() == 200
        db_updates = get_db_updates_response.get_result()
        assert db_updates is not None

    @needscredentials
    def test_head_replication_document(self):

        head_replication_document_response = self.cloudant_service.head_replication_document(
            doc_id='testString',
            if_none_match='testString'
        )

        assert head_replication_document_response.get_status_code() == 200

    @needscredentials
    def test_head_scheduler_job(self):

        head_scheduler_job_response = self.cloudant_service.head_scheduler_job(
            job_id='testString'
        )

        assert head_scheduler_job_response.get_status_code() == 200

    @needscredentials
    def test_post_replicate(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {
            'n': 1,
            'partitioned': True,
            'q': 1
        }

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {
            'api_key': 'testString'
        }

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {
            'iam': replication_database_auth_iam_model
        }

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {
            'auth': replication_database_auth_model,
            'headers': {},
            'url': 'testString'
        }

        # Construct a dict representation of a UserContext model
        user_context_model = {
            'db': 'testString',
            'name': 'testString',
            'roles': ['_reader']
        }

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'cancel': True,
            'checkpoint_interval': 0,
            'connection_timeout': 0,
            'continuous': True,
            'create_target': True,
            'create_target_params': replication_create_target_parameters_model,
            'doc_ids': ['testString'],
            'filter': 'testString',
            'http_connections': 1,
            'query_params': {},
            'retries_per_request': 0,
            'selector': {},
            'since_seq': 'testString',
            'socket_options': 'testString',
            'source': replication_database_model,
            'source_proxy': 'testString',
            'target': replication_database_model,
            'target_proxy': 'testString',
            'use_checkpoints': True,
            'user_ctx': user_context_model,
            'worker_batch_size': 1,
            'worker_processes': 1,
            'foo': { 'foo': 'bar' }
        }

        post_replicate_response = self.cloudant_service.post_replicate(
            replication_document=replication_document_model
        )

        assert post_replicate_response.get_status_code() == 200
        replication_result = post_replicate_response.get_result()
        assert replication_result is not None

    @needscredentials
    def test_get_replication_document(self):

        get_replication_document_response = self.cloudant_service.get_replication_document(
            doc_id='testString',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            conflicts=True,
            deleted_conflicts=True,
            latest=True,
            local_seq=True,
            meta=True,
            open_revs=['testString'],
            rev='testString',
            revs=True,
            revs_info=True
        )

        assert get_replication_document_response.get_status_code() == 200
        replication_document = get_replication_document_response.get_result()
        assert replication_document is not None

    @needscredentials
    def test_put_replication_document(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {
            'n': 1,
            'partitioned': True,
            'q': 1
        }

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {
            'api_key': 'testString'
        }

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {
            'iam': replication_database_auth_iam_model
        }

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {
            'auth': replication_database_auth_model,
            'headers': {},
            'url': 'http://myserver.example:5984/foo-db'
        }

        # Construct a dict representation of a UserContext model
        user_context_model = {
            'db': 'testString',
            'name': 'john',
            'roles': ['_reader']
        }

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'cancel': False,
            'checkpoint_interval': 4500,
            'connection_timeout': 15000,
            'continuous': True,
            'create_target': True,
            'create_target_params': replication_create_target_parameters_model,
            'doc_ids': ['testString'],
            'filter': 'ddoc/my_filter',
            'http_connections': 10,
            'query_params': {},
            'retries_per_request': 3,
            'selector': {},
            'since_seq': '34-g1AAAAGjeJzLYWBgYMlgTmGQT0lKzi9KdU',
            'socket_options': '[{keepalive, true}, {nodelay, false}]',
            'source': replication_database_model,
            'source_proxy': 'http://my-source-proxy.example:8888',
            'target': replication_database_model,
            'target_proxy': 'http://my-target-proxy.example:8888',
            'use_checkpoints': False,
            'user_ctx': user_context_model,
            'worker_batch_size': 400,
            'worker_processes': 3,
            'foo': { 'foo': 'bar' }
        }

        put_replication_document_response = self.cloudant_service.put_replication_document(
            doc_id='testString',
            replication_document=replication_document_model,
            if_match='testString',
            batch='ok',
            new_edits=True,
            rev='testString'
        )

        assert put_replication_document_response.get_status_code() == 201
        document_result = put_replication_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_get_scheduler_docs(self):

        get_scheduler_docs_response = self.cloudant_service.get_scheduler_docs(
            limit=0,
            skip=0,
            states=['initializing']
        )

        assert get_scheduler_docs_response.get_status_code() == 200
        scheduler_docs_result = get_scheduler_docs_response.get_result()
        assert scheduler_docs_result is not None

    @needscredentials
    def test_get_scheduler_document(self):

        get_scheduler_document_response = self.cloudant_service.get_scheduler_document(
            doc_id='testString'
        )

        assert get_scheduler_document_response.get_status_code() == 200
        scheduler_document = get_scheduler_document_response.get_result()
        assert scheduler_document is not None

    @needscredentials
    def test_get_scheduler_jobs(self):

        get_scheduler_jobs_response = self.cloudant_service.get_scheduler_jobs(
            limit=0,
            skip=0
        )

        assert get_scheduler_jobs_response.get_status_code() == 200
        scheduler_jobs_result = get_scheduler_jobs_response.get_result()
        assert scheduler_jobs_result is not None

    @needscredentials
    def test_get_scheduler_job(self):

        get_scheduler_job_response = self.cloudant_service.get_scheduler_job(
            job_id='testString'
        )

        assert get_scheduler_job_response.get_status_code() == 200
        scheduler_job = get_scheduler_job_response.get_result()
        assert scheduler_job is not None

    @needscredentials
    def test_get_session_information(self):

        get_session_information_response = self.cloudant_service.get_session_information()

        assert get_session_information_response.get_status_code() == 200
        session_information = get_session_information_response.get_result()
        assert session_information is not None

    @needscredentials
    def test_get_security(self):

        get_security_response = self.cloudant_service.get_security(
            db='testString'
        )

        assert get_security_response.get_status_code() == 200
        security = get_security_response.get_result()
        assert security is not None

    @needscredentials
    def test_put_security(self):

        # Construct a dict representation of a SecurityObject model
        security_object_model = {
            'names': ['testString'],
            'roles': ['testString']
        }

        put_security_response = self.cloudant_service.put_security(
            db='testString',
            admins=security_object_model,
            members=security_object_model,
            cloudant={},
            couchdb_auth_only=True
        )

        assert put_security_response.get_status_code() == 200
        ok = put_security_response.get_result()
        assert ok is not None

    @needscredentials
    def test_post_api_keys(self):

        post_api_keys_response = self.cloudant_service.post_api_keys()

        assert post_api_keys_response.get_status_code() == 201
        api_keys_result = post_api_keys_response.get_result()
        assert api_keys_result is not None

    @needscredentials
    def test_put_cloudant_security_configuration(self):

        # Construct a dict representation of a SecurityObject model
        security_object_model = {
            'names': ['testString'],
            'roles': ['testString']
        }

        put_cloudant_security_configuration_response = self.cloudant_service.put_cloudant_security_configuration(
            db='testString',
            cloudant={},
            admins=security_object_model,
            members=security_object_model,
            couchdb_auth_only=True
        )

        assert put_cloudant_security_configuration_response.get_status_code() == 200
        ok = put_cloudant_security_configuration_response.get_result()
        assert ok is not None

    @needscredentials
    def test_get_cors_information(self):

        get_cors_information_response = self.cloudant_service.get_cors_information()

        assert get_cors_information_response.get_status_code() == 200
        cors_configuration = get_cors_information_response.get_result()
        assert cors_configuration is not None

    @needscredentials
    def test_put_cors_configuration(self):

        put_cors_configuration_response = self.cloudant_service.put_cors_configuration(
            origins=['testString'],
            allow_credentials=True,
            enable_cors=True
        )

        assert put_cors_configuration_response.get_status_code() == 200
        ok = put_cors_configuration_response.get_result()
        assert ok is not None

    @needscredentials
    def test_head_attachment(self):

        head_attachment_response = self.cloudant_service.head_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            if_none_match='testString',
            rev='testString'
        )

        assert head_attachment_response.get_status_code() == 200

    @needscredentials
    def test_get_attachment(self):

        get_attachment_response = self.cloudant_service.get_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            if_none_match='testString',
            range='testString',
            rev='testString'
        )

        assert get_attachment_response.get_status_code() == 200
        result = get_attachment_response.get_result()
        assert result is not None

    @needscredentials
    def test_put_attachment(self):

        put_attachment_response = self.cloudant_service.put_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            attachment=io.BytesIO(b'This is a mock file.').getvalue(),
            content_type='testString',
            if_match='testString',
            rev='testString'
        )

        assert put_attachment_response.get_status_code() == 201
        document_result = put_attachment_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_get_local_document(self):

        get_local_document_response = self.cloudant_service.get_local_document(
            db='testString',
            doc_id='testString',
            accept='application/json',
            if_none_match='testString',
            attachments=True,
            att_encoding_info=True,
            atts_since=['testString'],
            local_seq=True
        )

        assert get_local_document_response.get_status_code() == 200
        document = get_local_document_response.get_result()
        assert document is not None

    @needscredentials
    def test_put_local_document(self):

        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True
        }

        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1
        }

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available'
        }

        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'foo': { 'foo': 'bar' }
        }

        put_local_document_response = self.cloudant_service.put_local_document(
            db='testString',
            doc_id='testString',
            document=document_model,
            content_type='application/json',
            batch='ok'
        )

        assert put_local_document_response.get_status_code() == 201
        document_result = put_local_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_post_local_docs(self):

        post_local_docs_response = self.cloudant_service.post_local_docs(
            db='testString',
            att_encoding_info=True,
            attachments=True,
            conflicts=True,
            descending=True,
            include_docs=True,
            inclusive_end=True,
            limit=0,
            skip=0,
            update_seq=True,
            endkey='testString',
            key='testString',
            keys=['testString'],
            startkey='testString',
            accept='application/json'
        )

        assert post_local_docs_response.get_status_code() == 200
        all_docs_result = post_local_docs_response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_local_docs_queries(self):

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': True,
            'attachments': True,
            'conflicts': True,
            'descending': True,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': True,
            'endkey': 'testString',
            'key': 'testString',
            'keys': ['testString'],
            'startkey': 'testString'
        }

        post_local_docs_queries_response = self.cloudant_service.post_local_docs_queries(
            db='testString',
            queries=[all_docs_query_model],
            accept='application/json'
        )

        assert post_local_docs_queries_response.get_status_code() == 200
        all_docs_queries_result = post_local_docs_queries_response.get_result()
        assert all_docs_queries_result is not None

    @needscredentials
    def test_post_missing_revs(self):

        post_missing_revs_response = self.cloudant_service.post_missing_revs(
            db='testString',
            document_revisions={}
        )

        assert post_missing_revs_response.get_status_code() == 200
        missing_revs_result = post_missing_revs_response.get_result()
        assert missing_revs_result is not None

    @needscredentials
    def test_post_revs_diff(self):

        post_revs_diff_response = self.cloudant_service.post_revs_diff(
            db='testString',
            document_revisions={}
        )

        assert post_revs_diff_response.get_status_code() == 200
        dict = post_revs_diff_response.get_result()
        assert dict is not None

    @needscredentials
    def test_get_shards_information(self):

        get_shards_information_response = self.cloudant_service.get_shards_information(
            db='testString'
        )

        assert get_shards_information_response.get_status_code() == 200
        shards_information = get_shards_information_response.get_result()
        assert shards_information is not None

    @needscredentials
    def test_get_document_shards_info(self):

        get_document_shards_info_response = self.cloudant_service.get_document_shards_info(
            db='testString',
            doc_id='testString'
        )

        assert get_document_shards_info_response.get_status_code() == 200
        document_shard_info = get_document_shards_info_response.get_result()
        assert document_shard_info is not None

    @needscredentials
    def test_get_active_tasks(self):

        get_active_tasks_response = self.cloudant_service.get_active_tasks()

        assert get_active_tasks_response.get_status_code() == 200
        list_active_task = get_active_tasks_response.get_result()
        assert list_active_task is not None

    @needscredentials
    def test_get_up_information(self):

        get_up_information_response = self.cloudant_service.get_up_information()

        assert get_up_information_response.get_status_code() == 200
        up_information = get_up_information_response.get_result()
        assert up_information is not None

    @needscredentials
    def test_delete_replication_document(self):

        delete_replication_document_response = self.cloudant_service.delete_replication_document(
            doc_id='testString',
            if_match='testString',
            batch='ok',
            rev='testString'
        )

        assert delete_replication_document_response.get_status_code() == 201
        document_result = delete_replication_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_local_document(self):

        delete_local_document_response = self.cloudant_service.delete_local_document(
            db='testString',
            doc_id='testString',
            batch='ok'
        )

        assert delete_local_document_response.get_status_code() == 200
        document_result = delete_local_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_index(self):

        delete_index_response = self.cloudant_service.delete_index(
            db='testString',
            ddoc='testString',
            type='json',
            index='testString'
        )

        assert delete_index_response.get_status_code() == 200
        ok = delete_index_response.get_result()
        assert ok is not None

    @needscredentials
    def test_delete_document(self):

        delete_document_response = self.cloudant_service.delete_document(
            db='testString',
            doc_id='testString',
            if_match='testString',
            batch='ok',
            rev='testString'
        )

        assert delete_document_response.get_status_code() == 200
        document_result = delete_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_design_document(self):

        delete_design_document_response = self.cloudant_service.delete_design_document(
            db='testString',
            ddoc='testString',
            if_match='testString',
            batch='ok',
            rev='testString'
        )

        assert delete_design_document_response.get_status_code() == 200
        document_result = delete_design_document_response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_database(self):

        delete_database_response = self.cloudant_service.delete_database(
            db='testString'
        )

        assert delete_database_response.get_status_code() == 200
        ok = delete_database_response.get_result()
        assert ok is not None

    @needscredentials
    def test_delete_attachment(self):

        delete_attachment_response = self.cloudant_service.delete_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            rev='testString',
            batch='ok'
        )

        assert delete_attachment_response.get_status_code() == 201
        document_result = delete_attachment_response.get_result()
        assert document_result is not None
