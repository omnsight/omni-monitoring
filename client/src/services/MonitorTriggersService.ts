/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { MonitorTrigger } from '../models/MonitorTrigger';
import type { MonitorTriggerMainData } from '../models/MonitorTriggerMainData';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class MonitorTriggersService {
    /**
     * Create Monitor Trigger
     * @param requestBody
     * @param authorization
     * @returns MonitorTrigger Successful Response
     * @throws ApiError
     */
    public static createMonitorTriggerMonitorTriggersPost(
        requestBody: MonitorTriggerMainData,
        authorization?: (string | null),
    ): CancelablePromise<MonitorTrigger> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/monitor-triggers',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Monitor Trigger
     * @param authorization
     * @returns MonitorTrigger Successful Response
     * @throws ApiError
     */
    public static getMonitorTriggerMonitorTriggersGet(
        authorization?: (string | null),
    ): CancelablePromise<MonitorTrigger> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/monitor-triggers',
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Monitor Trigger
     * @param authorization
     * @returns void
     * @throws ApiError
     */
    public static deleteMonitorTriggerMonitorTriggersDelete(
        authorization?: (string | null),
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/monitor-triggers',
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
