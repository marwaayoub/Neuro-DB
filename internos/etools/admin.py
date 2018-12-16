
from django.contrib import admin

from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin

from .models import PartnerOrganization, Agreement, PCA, PartnerStaffMember, Travel


class PartnerStaffMemberInline(admin.TabularInline):
    model = PartnerStaffMember
    max_num = 99
    min_num = 0
    extra = 1
    verbose_name = 'Partner staff member'
    verbose_name_plural = 'Partner staff members'

    fields = (
        'title',
        'first_name',
        'last_name',
        'email',
        'phone',
        'active',
    )


class PartnerOrganizationResource(resources.ModelResource):
    class Meta:
        model = PartnerOrganization
        fields = (
            'id',
            'vendor_number',
            'name',
            'short_name',
            'partner_type',
            'cso_type',
            'rating',
            'shared_partner',
            'email',
            'phone_number',
        )
        export_order = fields


class PartnerOrganizationAdmin(ImportExportModelAdmin):
    resource_class = PartnerOrganizationResource

    readonly_fields = (
        'vendor_number',
        'name',
        'short_name',
        'partner_type',
        'cso_type',
        'rating',
        'shared_partner',
        'email',
        'phone_number',
    )

    fields = (
        'vendor_number',
        'name',
        'short_name',
        'partner_type',
        'cso_type',
        'rating',
        'shared_partner',
        'email',
        'phone_number',
    )
    search_fields = (
        'name',
    )

    inlines = [PartnerStaffMemberInline, ]


class AgreementResource(resources.ModelResource):
    class Meta:
        model = Agreement
        fields = (
            'id',
            'partner_name',
            'agreement_type',
            'agreement_number',
            'start',
            'end',
            'signed_by_unicef_date',
            'signed_by_partner_date',
        )
        export_order = fields


class AgreementAdmin(ImportExportModelAdmin):
    resource_class = AgreementResource


class PCAResource(resources.ModelResource):
    class Meta:
        model = PCA
        fields = (
            'id',
            'number',
            'document_type',
            'partner_name',
            'status',
            'title',
            'start',
            'end',
            'country_programme',
            'signed_by_unicef_date',
            'signed_by_partner_date',
        )
        export_order = fields


class PCAAdmin(ImportExportModelAdmin):
    resource_class = PCAResource

    list_display = (
        'number',
        'partner',
        'partner_name',
        'document_type',
        'country_programme',
        'start',
        'end',
    )

    list_filter = (
        'partner',
        'document_type',
        'country_programme',
    )

    search_fields = (
        'number',
        # 'partner',
    )


class PartnerStaffMemberResource(resources.ModelResource):
    class Meta:
        model = PartnerStaffMember
        fields = (
        )
        export_order = fields


class PartnerStaffMemberAdmin(ImportExportModelAdmin):
    resource_class = PartnerStaffMemberResource
    fields = (
        'title',
        'first_name',
        'last_name',
        'email',
        'phone',
        'active',
    )
    list_display = (
        'partner',
        'title',
        'first_name',
        'last_name',
        'email',
        'phone',
        'active',
    )
    list_filter = (
        'partner',
        'active',
    )
    search_fields = (
        'partner__name',
        'first_name',
        'last_name',
        'email',
        'phone',
    )


admin.site.register(PartnerOrganization, PartnerOrganizationAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(PCA, PCAAdmin)
admin.site.register(Travel)
admin.site.register(PartnerStaffMember, PartnerStaffMemberAdmin)
