#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 Thiaguindozap
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

lib_fixups: lib_fixups_user_type = {}

blob_fixups: blob_fixups_user_type = {
    'product/etc/permissions/vendor.qti.hardware.data.connection-V1.0-java.xml': blob_fixup()
        .regex_replace('xml version="2.0"', 'xml version="1.0"'),
    'product/etc/permissions/vendor.qti.hardware.data.connection-V1.1-java.xml': blob_fixup()
        .regex_replace('xml version="2.0"', 'xml version="1.0"'),
    'system_ext/etc/permissions/moto-telephony.xml': blob_fixup()
        .regex_replace('system', 'system/system_ext'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/libdpps.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    # Camera fixups
    'vendor/lib64/camera/components/com.qti.node.gpu.so': blob_fixup()
        .regex_replace('camera.mot.is.coming.cts', 'vendor.camera.coming.cts'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .regex_replace('camera.mot.is.coming.cts', 'vendor.camera.coming.cts'),
    'vendor/lib64/hw/com.qti.chi.override.so': blob_fixup()
        .regex_replace('camera.mot.is.coming.cts', 'vendor.camera.coming.cts'),
}

namespace_imports = [
    'device/motorola/sm6150-common',
    'hardware/qcom-caf/sm8150',
    'hardware/motorola',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

module = ExtractUtilsModule(
    'sm6150-common',
    'motorola',       
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

