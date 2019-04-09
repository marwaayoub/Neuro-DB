from __future__ import absolute_import, unicode_literals

import os
import datetime
import calendar
from django.db.models import Q
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse

from internos.backends.djqscsv import render_to_csv_response
from braces.views import GroupRequiredMixin, SuperuserRequiredMixin
from .models import PartnerOrganization, Engagement
from internos.users.models import Section
from internos.activityinfo.models import Database


class PartnerProfileView(TemplateView):

    template_name = 'etools/partner_profile.html'

    def get_context_data(self, **kwargs):
        databases = Database.objects.filter(reporting_year__current=True).exclude(ai_id=10240).order_by('label')
        engagements = Engagement.objects.all()
        spot_checks = engagements.filter(engagement_type='sc')
        audits = engagements.filter(engagement_type='audit')
        micro_assessments = engagements.filter(engagement_type='ma')
        special_audits = engagements.filter(engagement_type='sa')

        partners = engagements.values('partner_id', 'partner__name').distinct()
        print(partners)

        return {
            'databases': databases,
            'partners': partners,
            'nbr_spot_checks': spot_checks.count(),
            'nbr_audits': audits.count(),
            'nbr_micro_assessments': micro_assessments.count(),
            'nbr_special_audits': special_audits.count(),
        }
